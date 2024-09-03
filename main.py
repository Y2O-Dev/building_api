from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    publish: bool = True
    rating: Optional[int] = None

my_posts = [
    {
        "titie": "title of post 1", 
        "content": "contents of post 1",
        "id": 1
    },
    {
        "title": "favourite foods",
        "content": "I like amala",
        "id": 2
    }

]

# @=decorator
@app.get("/")
async def root():
    return {"message": "Hello World, I'm learning API"}

@app.get("/posts")
async def get_post():
    return {"data": my_posts}

# The first path operation that matches will run

@app.post("/posts")
def create_post(new_post: Post):    #extraction of data from the body 
    print(new_post)
    print(new_post.dict())
    return{"Data": new_post}

#return{"Create": "New post successfully"}