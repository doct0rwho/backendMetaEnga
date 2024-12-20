from sqlmodel import create_engine, Session

DATABASE_URL = "postgresql://postgres:1111@ec2-16-171-113-28.eu-north-1.compute.amazonaws.com/db"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
