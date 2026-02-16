from typing import Generator
from pymongo import MongoClient
from app.core.config import settings

# Expect `DATABASE_URL` to be a MongoDB URI. If it contains a database name
# (e.g. mongodb://host:port/dbname) the client will expose that as the default
# database. Otherwise we fall back to a database named after the project.
client = MongoClient(settings.DATABASE_URL)
try:
    db = client.get_default_database()
except Exception:
    db = client[settings.PROJECT_NAME.lower()]


def get_db() -> Generator:
    # For pymongo we can yield the Database instance directly
    try:
        yield db
    finally:
        # pymongo client is long-lived; do not close here
        pass
