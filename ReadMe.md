#  Employee Management API

A Django-based backend system to manage **Employees, Departments, Attendance**, and **Performance Reviews**. Built with **Django REST Framework**, **PostgreSQL**, and **Faker**.

---

## 📌 Project Overview

This project includes:

- Models for **Employee**, **Department**, **Attendance**, and **Performance**
- REST APIs with **CRUD** operations using Django REST Framework
- Authentication via **TokenAuth** or **JWT**
- API **filtering**, **pagination**, and **sorting** support
- Swagger API documentation using `drf-yasg`

---

## ⚙️ Setup Instructions

### 1. Create a Virtual Environment

```bash
python -m venv venv
# Activate the environment

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```
### 2. Clone the Repository
```bash
git clone https://github.com/AYAZ2006/Intern-backend.git
cd employee_project
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 6. Run the Server
```bash
python manage.py runserver
```

## 🗂️ Project Folder Structure

```bash
employee_project/
│
├── employee_project/                # Main Django project folder
│   ├── __init__.py
│   ├── settings.py                  # Project settings
│   ├── urls.py                      # Root URL config
│   └── wsgi.py / asgi.py
│
├── employees/                       # Employee app
│   ├── models.py                    # Employee & Department models
│   ├── serializers.py               # DRF serializers
│   ├── views.py                     # API views
│   ├── urls.py                      # App-specific URLs
│   ├── admin.py                     # Admin config
│   └── management/
│       └── commands/
│           └── seed_data.py         # Faker seed script
│
├── attendance/                      # Attendance app
│   ├── models.py, views.py, ...
│
├── performance/                     # Performance app
│   ├── models.py, views.py, ...
│
├── departments/                     # Departments app (if separate)
│   ├── models.py, views.py, ...
│
├── db.sqlite3 / postgres            # Local DB (use PostgreSQL in production)
├── manage.py                        # Django CLI utility
├── requirements.txt                 # Project dependencies
└── README.md                        # Project documentation
```

