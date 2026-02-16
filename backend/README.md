# Backend — WebSentinel

Quick dev steps:

- Create a virtualenv and install dependencies:
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```
- Copy `.env.example` to `.env` and edit if needed:
```bash
cd backend
copy .env.example .env   # Windows
```
- Run the dev server:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Notes:
- The app creates DB tables on startup for development. For production use Alembic migrations.
- Authentication endpoints: `/api/v1/register`, `/api/v1/login` (JSON body with `email` and `password`).
