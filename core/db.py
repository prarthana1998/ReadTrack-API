from sqlmodel import SQLModel, create_engine
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/bookbound"

engine = create_engine(DATABASE_URL, echo=True)
def init_db():
    SQLModel.metadata.create_all(engine)