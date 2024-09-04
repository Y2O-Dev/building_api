from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

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
    new_post_dict = new_post.dict()
    new_post_dict["id"] = randrange(1, 100000)
    my_posts.append(new_post_dict)
    print(new_post.dict())
    return{"Data": new_post_dict}

#return{"Create": "New post successfully"}