<!-- Copilot instructions for AI coding agents working on SucroSec -->
# Copilot Instructions — SucroSec

Purpose: give an AI coding agent just-enough, repository-specific context to be productive fast.

- **Big picture**: backend is a FastAPI service (see `backend/requirements.txt`), frontend is React (`frontend/`). The backend code lives under `backend/app/` split into `api/`, `services/`, `models/`, `schemas/`, `db/`, and `core/`.
- **Data & infra**: SQLAlchemy 2.0 + PostgreSQL (`psycopg2-binary`), migrations via Alembic (look in `backend/app/db`). Auth uses JWT-related libraries (`python-jose`, `passlib`, `bcrypt`) and environment config uses `python-dotenv`.
- **Security tooling**: repo docs state SAST is Semgrep and DAST is OWASP ZAP (see `docs/architecture.md`).

How the backend is organized (patterns to follow)
- `api/`: HTTP routers and endpoint wiring — keep endpoints thin; call `services/*` for business logic.
- `services/`: core business logic and transactional code. Prefer small service functions that accept/return domain models or pydantic schemas.
- `models/`: SQLAlchemy ORM models. Use SQLAlchemy 2.0 idioms (session management likely in `db/`).
- `schemas/`: Pydantic v2 schemas (input/output shapes). Use these for validation and response models in routers.
- `db/`: DB engine, session factory, and migration scripts. Any DB change should include Alembic migration updates here.

Run & dev workflow (explicit commands)
- Install deps: from repository root:
```
cd backend
pip install -r requirements.txt
```
- Run backend dev server (module path is relative to `backend`):
```
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
- If adding DB migrations:
```
cd backend
alembic revision --autogenerate -m "desc"
alembic upgrade head
```
Note: `main.py` is the FastAPI entrypoint (under `backend/app/main.py`). If `main.py` is changed, ensure the `app` ASGI instance variable remains named `app` for the `uvicorn` invocation above.

Project-specific conventions
- Keep business logic inside `services/` rather than embedding SQL in controllers.
- Use `schemas/` for all public request/response shapes; convert between ORM and schema using explicit constructors/helpers in `services/` or `models` modules.
- Favor small, testable functions in `services/` to make future unit tests straightforward.
- Environment variables are used for secrets/DB URLs; prefer loading via `python-dotenv` in `core` or `main`.

Integration points & external deps
- Frontend <-> Backend: standard REST JSON; check `api/` routers for specific route names and expected payloads.
- Database: PostgreSQL (connection via SQLAlchemy engine in `db/`).
- Auth: JWT tokens (signing via `python-jose`), password hashing via `passlib`/`bcrypt`.
- Websockets: `websockets` and `uvicorn` are in requirements — search `api` or `core` for realtime endpoints.

What agents must not assume
- Don't assume tests or linters are present — run and add thoughtfully.
- `main.py` may be empty or unimplemented; confirm the ASGI `app` exists before restarting servers.

How to make safe changes
- For DB migrations, always add an Alembic revision and run `alembic upgrade head` locally.
- When adding endpoints, update `schemas/` and keep controllers thin; add/update a `services/` function and unit tests if possible.
- Preserve existing import paths (repo runs with `backend` as working dir for `uvicorn app.main:app`).

Quick references
- Architecture overview: [docs/architecture.md](docs/architecture.md)
- Backend entry & packages: [backend/requirements.txt](backend/requirements.txt)
- Backend app root: [backend/app/main.py](backend/app/main.py)
- Key dirs: [backend/app/api](backend/app/api), [backend/app/services](backend/app/services), [backend/app/models](backend/app/models), [backend/app/schemas](backend/app/schemas), [backend/app/db](backend/app/db)

If anything here is unclear or missing, ask a concise question (e.g., “Where are Alembic env/migrations?”) and I will inspect files and update these notes.
