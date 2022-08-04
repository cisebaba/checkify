<h1 align="center">Checkify - Task Management System 📝</h1>

Checkify is a full-stack web app to manage the company’s to-do lists. 
- Implemented Django backend to take advantage of class inheritance for simple creation of submission forms.
- Architected the front-end using Django templates to make a smooth transition to interactive applications. Checkify is a full-stack web app to manage the company’s to-do lists. - Implemented Django backend to take advantage of class inheritance for simple creation of submission forms. - Architected the front-end using Django templates to make a smooth transition to interactive applications.
- Skills: Cascading Style Sheets (CSS) · HTML5 · Python (Programming Language) · Django · REST APIs
<hr>
<br>

## Overview 
<div align="center"><br />
    <h3 align="center">Landing Page and Project Detail Page</h3>
  ![Image](overviw_img/landing_page.png)
  <img src="https://raw.githubusercontent.com/jeelason/zah-wines/main/ss/z-2.png" alt="wine list" width='40%'/><br />
    <h3 align="center">submit new wine, guest submissions</h3>
  <img src="https://raw.githubusercontent.com/jeelason/zah-wines/main/ss/z-3.png" alt="wine form" width='40%' />
    <img src="https://raw.githubusercontent.com/jeelason/zah-wines/main/ss/z-4.png" alt="admin-tasks" width='40%' /><br />
    <h3 align="center">Admin functionality to view and mark inquiries as complete</h3>
    <img src="https://raw.githubusercontent.com/jeelason/zah-wines/main/ss/z-5.png" alt="admin-tasks" width='40%' /><br />
</div>


## For setup

Create a virtual python environment <br />
`python -m venv .venv`

Activate the environment<br />
`source .venv/bin/activate`

Update pip<br />
`python -m pip install --upgrade pip`

Install requirements<br />
`pip install -r requirements.txt`

Run migrations<br />
`python manage.py migrate`

Runserver<br />
`python manage.py runserver`

Create superuser<br />
`python manage.py createsuperuser`

Access in browser <br />
`http://localhost:8000`