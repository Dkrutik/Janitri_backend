# Janitri Backend Assignment

## Overview
This project is a Django REST Framework backend for a simplified patient monitoring system.  
It allows users to register/login, manage patients, and record/retrieve heart rate data from devices.

---

## Project Objectives

- Create a Django project with RESTful APIs.
- Manage users, patients, and heart rate records.
- Implement secure authentication and authorization.
- Handle data efficiently with validation and error handling.
- Implement pagination and filtering where large datasets exist.
- Document APIs and write unit tests for all major functionalities.

---

## Data Models

- **User**: Manages user information.
- **Patient**: Stores patient information linked to a user.
- **HeartRate**: Records heart rate data for patients.

Relationships:
- A **User** can have multiple **Patients**.
- Each **Patient** can have multiple **HeartRate** records.

---

## Setup Instructions

1. **Clone the repository**


git clone  https://github.com/Dkrutik/Janitri_backend.git

## Setup Instructions
1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start server: `python manage.py runserver`

## API Endpoints
- `POST /api/register/` → Register new user
- `POST /api/login/` → Login (get JWT token)
- `POST /api/token/refresh/` → Refresh JWT token
- `GET/POST /api/patients/` → List or add patient
- `GET /api/patients/<id>/` → Retrieve patient details
- `GET/POST /api/heart-rates/` → List or add heart rate

## Running Tests
python manage.py test

## Notes
- JWT Authentication is used.
- SQLite is default DB (can switch to MySQL/PostgreSQL in settings).
