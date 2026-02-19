from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Gugenheim%408421@localhost:5432/bookstore"

engine = create_engine(SQLALCHEMY_DATABASE_URL) # creating engine to connect to the DB

# using sessionmaker to perform actions on our DB. autocommit and autoflush set to TRUE which means unless we are specifying 
# want to Commit the changes, the changes will not be reflected to the DB. & bind means we are binding the engine to the DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() # to create the tables in the DB

def get_db():
    """
    This function creates a DB session
    db: session object. through this we can open a session, create the tables in the DB. 
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close


def create_table():
    Base.metadata.create_all(bind=engine)
