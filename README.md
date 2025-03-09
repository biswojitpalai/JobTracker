# AI-Powered Job Application Tracker

## 🚀 Overview
**JobTrack** is an AI-powered job application tracking system designed to help job seekers organize their job search efficiently. It provides a seamless experience for managing job applications, analyzing resumes using AI, and tracking progress with real-time insights.

### 🔹 Why JobTrack?
- **Stay Organized:** Keep track of job applications with a structured workflow.
- **AI-Powered Insights:** Get instant resume analysis and job match scores.
- **Real-Time Analytics:** Monitor application trends and identify key opportunities.

## 🏗️ Project UI/UX
  ![JobTrack Dashboard Preview](https://github.com/biswojitpalai/JobTracker/blob/main/images/homepage.png)
  ![alt text](https://github.com/biswojitpalai/JobTracker/blob/main/images/signup%20page.png)
  ![alt text](https://github.com/biswojitpalai/JobTracker/blob/main/images/Signin%20page.png)
  ![alt text](https://github.com/biswojitpalai/JobTracker/blob/main/images/Application%20page.png)
  ![alt text](https://github.com/biswojitpalai/JobTracker/blob/main/images/stats%20page.png)
  ![alt text](https://github.com/biswojitpalai/JobTracker/blob/main/images/ResumeAnalysis%20page.png)
  ![alt text](https://github.com/biswojitpalai/JobTracker/blob/main/images/ResumeAnalysis%20page%202.png)

  
## 🛠 Technology Stack
### Frontend:
- **React.js** – Fast and modern UI framework
- **Tailwind CSS** – Utility-first styling
- **Axios** – API communication
- **React Router** – Client-side navigation

### Backend:
- **Django 5.0** – Backend framework
- **Django REST Framework (DRF)** – API development
- **Simple JWT** – Secure authentication
- **Python 3.10+** – Backend language

### AI Integration:
- **Gemini 2.0 Flash API** – AI-powered resume analysis
- **PDFPlumber & python-docx** – Resume file parsing

## 📥 Installation & Setup
### 1️⃣ Clone Repository:
```bash
git clone https://github.com/biswojitpalai/JobTracker
cd JobTracker
```

### 2️⃣ Backend Setup:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
## install all required dependencies

Run migrations and start the server:
```bash
python manage.py migrate
python manage.py runserver
```

### 3️⃣ Frontend Setup:
```bash
cd ../frontend
npm install
npm run dev
```
**Access Application:** `http://localhost:3000`

## 📘 User Guide
### 🔐 Authentication:
- Sign up with an email/username
- Log in securely with JWT authentication

### 📌 Managing Applications:
- **Add:** Click `+ New Application`
- **Edit:** Click the `✏️` (pencil) icon
- **Delete:** Click the `🗑️` (trash) icon
- **Track Status:** Drag and drop between columns

### 🤖 AI Resume Analysis:
- Upload a **PDF/Word** resume
- Paste the **job description**
- Get an **instant analysis**, including:
  - **Match Score (0-100%)**
  - **Key Strengths**
  - **Improvement Areas**
  - **Custom Suggestions**

### 📊 Statistics Dashboard:
- **Application Distribution** by status
- **Timeline Visualization** of job progress
- **Company Comparison** for better job insights
- **Skill Gap Analysis** to improve resumes

## 🌟 Key Features
✅ Secure **JWT Authentication**
✅ **PDF/Word Resume Parsing** & AI Analysis
✅ **Real-Time statistics**
✅ **Responsive**

## 📚 API Documentation
Access Swagger API Docs at:
```
http://localhost:8000/api/docs/
```

## 🤝 Contribution Guidelines
1. **Fork the repository**
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/new-feature
   ```
3. **Commit changes**:
   ```bash
   git commit -m 'Add new feature'
   ```
4. **Push to branch**:
   ```bash
   git push origin feature/new-feature
   ```
5. **Open a Pull Request**

## 📝 License
This project is open-source under the **MIT License**.

---

### 🎯 Let's Build a Smarter Job Search Together!
🚀 Star ⭐ this repo if you find it useful!

---

🔗 **Connect:** [GitHub](https://github.com/biswojitpalai/) | [LinkedIn](https://www.linkedin.com/in/biswojitpalai/)

