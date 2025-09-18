# Janitri Backend Assignment

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

## Notes
- JWT Authentication is used.
- SQLite is default DB (can switch to PostgreSQL in settings).
