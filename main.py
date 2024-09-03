from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

# @=decorator
@app.get("/")
async def root():
    return {"message": "Hello World, I'm learning API"}

@app.get("/post")
async def get_post():
    return {"This is your API request..."}

# The first path operation that matches will run

@app.post("/post")
def create_post(new_post: Post):    #extraction of data from the body 
    print(new_post.title)
    return{"new_post": "Data"}

#return{"Create": "New post successfully"}