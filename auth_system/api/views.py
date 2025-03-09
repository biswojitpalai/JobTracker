from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from rest_framework.decorators import api_view
import google.generativeai as genai
import os
import json
from rest_framework import generics, permissions
from rest_framework.views import APIView
import pdfplumber
from docx import Document
import io
import requests
import json
from django.conf import settings
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.throttling import UserRateThrottle

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(TokenObtainPairView):
    pass

class CardsView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        data = [
            {"title": "Saved", "content": "0 items saved"},
            {"title": "Sent", "content": "0 applications sent"},
            {"title": "Interviews", "content": "0 interviews scheduled"},
            {"title": "Finished", "content": "0 processes completed"},
        ]
        return Response(data)
    
class JobApplicationListCreate(generics.ListCreateAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class JobApplicationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return JobApplicationUpdateSerializer
        return JobApplicationSerializer


# Throttling for analysis endpoint
class AnalysisThrottle(UserRateThrottle):
    scope = 'resume_analysis'

class ResumeAnalysisView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    throttle_classes = [AnalysisThrottle]
    
    ALLOWED_TYPES = [
        'application/pdf',
        'application/msword',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    ]

    def parse_resume(self, file):
        """Parse PDF or Word resume content"""
        try:
            content_type = file.content_type
            
            if content_type == 'application/pdf':
                with pdfplumber.open(file) as pdf:
                    return '\n'.join([page.extract_text() for page in pdf.pages])
            
            elif content_type in ['application/msword', 
                                 'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
                document = Document(io.BytesIO(file.read()))
                return '\n'.join([para.text for para in document.paragraphs])
            
            raise ValueError("Unsupported file format")
            
        except Exception as e:
            raise ValueError(f"Error parsing resume: {str(e)}")

    def post(self, request):
        try:
            # Validate inputs
            if 'resume' not in request.FILES:
                return Response({'error': 'No resume file uploaded'}, status=400)
                
            if not request.data.get('jobDescription'):
                return Response({'error': 'Job description is required'}, status=400)

            resume_file = request.FILES['resume']
            
            # Validate file type
            if resume_file.content_type not in self.ALLOWED_TYPES:
                return Response({'error': 'Invalid file type. Only PDF and Word documents are allowed.'}, 
                              status=400)

            # Parse resume content
            resume_text = self.parse_resume(resume_file)
            
            # Prepare Gemini request
            job_desc = request.data['jobDescription']
            prompt = f"""Analyze this resume against the job description and return JSON with:
            - matchScore (0-100 number)
            - strengths (array of 3 strings)
            - improvements (array of 3 strings)
            - suggestions (array of 3 strings)
            
            Resume:
            {resume_text[:3000]}  # Limit to 3000 chars for safety
            
            Job Description:
            {job_desc[:2000]}"""  # Limit to 2000 chars

            # Call Gemini API
            response = requests.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=<your API Key>",
                json={
                    "contents": [{
                        "parts": [{"text": prompt}]
                    }]
                },
                timeout=30  # 30 seconds timeout
            )
            
            # Handle API errors
            response.raise_for_status()
            data = response.json()

            # Validate response structure
            if not data.get('candidates') or not data['candidates'][0].get('content'):
                return Response({'error': 'Invalid API response format'}, status=500)

            # Extract and clean response text
            response_text = data['candidates'][0]['content']['parts'][0]['text']
            json_str = response_text.strip().replace('```json', '').replace('```', '').strip()
            
            # Parse JSON safely
            try:
                analysis = json.loads(json_str)
                
                # Validate analysis structure
                required_keys = ['matchScore', 'strengths', 'improvements', 'suggestions']
                if not all(key in analysis for key in required_keys):
                    raise ValueError("Missing required analysis fields")
                    
                # Validate score range
                if not 0 <= analysis['matchScore'] <= 100:
                    raise ValueError("Invalid match score range")

            except (json.JSONDecodeError, ValueError) as e:
                return Response({'error': f'Analysis parsing failed: {str(e)}'}, status=500)

            return Response({'analysis': analysis})

        except requests.exceptions.RequestException as e:
            return Response({'error': f'API request failed: {str(e)}'}, status=503)
            
        except Exception as e:
            return Response({'error': f'Analysis failed: {str(e)}'}, status=500)
