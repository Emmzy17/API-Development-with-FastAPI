from fastapi import FastAPI


import models
from routers import posts, users, auth, vote
from database import engine, SessionLocal
app = FastAPI()


models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()






app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)