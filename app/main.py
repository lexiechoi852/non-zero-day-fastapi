from fastapi import FastAPI
from sqlmodel import Session, select
from app.database import engine

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/db-test")
def test_db():
    try:
        with Session(engine) as session:
            session.exec(select(1)).first()  # simple query
        return {"status": "database connected!"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}