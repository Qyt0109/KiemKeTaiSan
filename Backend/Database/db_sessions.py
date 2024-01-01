from Backend.Database.db_models import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Create an SQLite engine
# echo = True to logging any SQL query to console
engine = create_engine("sqlite:///Backend/Database/db.sqlite", echo=True)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)
# default_session = Session()