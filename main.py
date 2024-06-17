from fastapi import FastAPI
from schemas import Blog
from . import models
# from database import engine
app = FastAPI()
model = models.Base()
model.metadata.create_all(engine)

@app.post('/blog')
def create(req: Blog):
    return f'{req.title} - {req.body}'