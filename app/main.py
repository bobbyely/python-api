from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

# Create database if not exists 
#models.Base.metadata.create_all(bind=engine) # Now covered by alembic

# Allow origins
origins = ["*"]

# Create Fast API app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


# Dummy default route
@app.get("/")
def get_root():
    return {"message" : "This is root."}

