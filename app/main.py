from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware


import app.models
from app.routers import posts, users, auth, vote
from app.database import engine, SessionLocal
app = FastAPI()


#models.Base.metadata.create_all(bind=engine)
origins = []

app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"], 
    allow_headers = ["*"]

)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/', status_code=status.HTTP_200_OK)
def root():
    return {'message': 'Check out the docs to  see how to work with the Api @ \docs'}






app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)