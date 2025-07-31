# Employee Management API

A Django-based backend system to manage Employees, Departments, Attendance, and Performance reviews. Built with Django REST Framework, PostgreSQL, and Faker.

---

## 📌 Project Overview

This project includes:

- Employee, Department, Attendance, and Performance models.
- REST APIs for full CRUD operations using Django REST Framework.
- Authentication using TokenAuth or JWT.
- Filtering, pagination, and sorting support.
- Swagger API documentation using `drf-yasg`.

---

## ⚙️ Setup Instructions
python -m venv venv
source venv/bin/activate

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/employee_project.git
cd employee_project

Install Dependencies
pip install -r requirements.txt

API Usage Guide
🔑 Authentication
Supports Token Authentication or Simple JWT.

Add token to headers:
Authorization: Bearer <your_token>

🧑 Employees
GET /api/employees/

POST /api/employees/

GET /api/employees/<id>/

PUT /api/employees/<id>/

DELETE /api/employees/<id>/

Supports: ?department=1, ?date_joined__gte=2023-01-01

🏢 Departments
GET /api/departments/

POST /api/departments/

🕒 Attendance
GET /api/attendance/

POST /api/attendance/

📊 Performance
GET /api/performance/

POST /api/performance/
