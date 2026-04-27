from sqlalchemy import create_engine, MetaData

DATABASE_URL = "postgresql://postgres:layan00000@localhost:5432/skills_db"

engine = create_engine(DATABASE_URL, echo=True)

metadata = MetaData()