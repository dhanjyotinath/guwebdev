Web Development Skill Test Project  
Gauhati University – Web Developer Practical Exam**


Project Overview
This project was developed as part of a **Web Developer Skill Test**. It includes:

Flask-based web form application
WordPress-based website pages (UI/Content Management)



Features Implemented

Flask Application
- User Form with:
  - Name
  - Email (@gauhati.ac.in only)
  - Age
  - Gender (Radio Button)
  - Birth Date
  - File Upload (PDF/JPG)

- Validations:
  - Required fields
  - Email domain restriction
  - File type restriction

- File Upload:
  - Accepts PDF/JPG
  - Secure saving


WordPress Website
- Pages:
  - Home
  - News
  - Contact/Address

- Features:
  - Navigation menu
  - News section
  - Clean UI


- Python
- Flask
- Flask-WTF
- HTML/CSS
- WordPress


project/
│── app.py
│── forms.py
│── templates/
│── uploads/
│── README.md


Setup Instructions

1. Install dependencies:
pip install flask flask-wtf

2. Run app:
python app.py

3. Open browser:
http://127.0.0.1:5000/

Validation Rules

- Email must be @gauhati.ac.in
- File only PDF/JPG
- All fields required

Dhanjyoti Nath

Note
Created during web developer practical exam.

PART B DESIGN DECISION
Q4. 
A. REJECT
B. RISKD
C. SHORT TERM IMPLICATION
D. REMOVE ANIMATION PLUGIN
