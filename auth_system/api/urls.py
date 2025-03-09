from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('cards/', CardsView.as_view(), name='cards'),
    path('analyze-resume/', ResumeAnalysisView.as_view(), name='analyze-resume'),
     path('applications/', JobApplicationListCreate.as_view(), name='applications'),
    path('applications/<int:pk>/', JobApplicationRetrieveUpdateDestroy.as_view(), name='application-detail'),
]