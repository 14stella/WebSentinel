from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)


@app.get("/")
def read_root():
	return {"message": f"{settings.PROJECT_NAME} API"}


from app.api.health import router as health_router
from app.api.auth import router as auth_router
from app.db.session import db as mongo_db


app.include_router(health_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v1")


@app.get("/api/v1/ready")
def ready():
	return {"status": "ready"}


@app.on_event("startup")
def on_startup():
	# Ensure a unique index on users.email for lookup/uniqueness
	try:
		mongo_db.users.create_index("email", unique=True)
	except Exception:
		pass
