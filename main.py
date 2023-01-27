from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.params import Body
from typing import *

app = FastAPI()

#Schema Post whichnis extending the Base model 
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
def root():
    return {"message":"Hello"}

@app.get("/posts")
def get_post():
    return {"data":"This is your post"}

@app.post("/posts")
# # this method doesnot validate the data from the request  
# def create_post(payload: dict = Body(...)):
#     print(payload)
#     # print(payload["title"],"titleeeee")
#     print("hhhhhhhhhhhhhhhhhhhhh")
#     # return{"new_post": f"title {payload['title']} content: {payload['content']}"}
#     return{"new_post": "new post"}

# Using the schema to validate the data and process it 
def create_post(new_post: Post):
    #new post is a schema pidentic model 
    print(new_post)
    #to conver pydentic model to dict
    print(new_post.dict())
    print(new_post.rating,"hhhhhhhhhhhhhhhhhhhhh")
    # return{"new_post": f"title {new_post.title} content: {new_post.content}"}
    return{"new_post": 'new post'}
