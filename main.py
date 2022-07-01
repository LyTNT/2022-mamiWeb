from fastapi import FastAPI, Depends
import models #da tao module rieng
from database import engine
from routers import home
from starlette.staticfiles import StaticFiles

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

"""mounting means adding a completely independent application to a specific path, it handle everything under the path, 
but the path operations declared in that sub application."""
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(home.router)
# app.include_router(todo.router)