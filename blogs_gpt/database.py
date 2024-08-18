# database.py
from sqlmodel import SQLModel, create_engine
from .settings import DATABASE_URL

# Convert the database URL to use psycopg2
connection_string = str(DATABASE_URL).replace("postgresql", "postgresql+psycopg2")

# Create the engine for connecting to the database
engine = create_engine(connection_string)

def create_db_and_tables():
    """Create the database tables."""
    SQLModel.metadata.create_all(engine)
