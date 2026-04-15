from fastapi import FastAPI ,HTTPException
from app.schemas import PostCreate ,PostResponse,PostPatch

app=FastAPI()

text_posts = {
    1: {'name': 'siddharth', 'age': 22, 'email': 'siddharthdoshi53@gmail.com'},
    2: {'name': 'ritesh',  'age': 22, 'email': 'riteshchougule96@gmail.com'},
    3: {'name': 'aryan',  'age': 22, 'email': 'aryankagawde123@gmail.com'},
    4: {'name': 'meera',  'age': 30, 'email': 'meera28@gmail.com'},
    5: {'name': 'karan',  'age': 30, 'email': 'karan15@icloud.com'},
    6: {'name': 'tanya',  'age': 28, 'email': 'tanya65@gmail.com'},
    7: {'name': 'aryan',  'age': 19, 'email': 'aryan99@icloud.com'},
    8: {'name': 'vikram', 'age': 19, 'email': 'vikram63@gmail.com'},
    9: {'name': 'isha',   'age': 32, 'email': 'isha38@yahoo.com'},
    10: {'name': 'suresh', 'age': 23, 'email': 'suresh65@icloud.com'},
    11: {'name': 'sneha', 'age': 21, 'email': 'sneha54@gmail.com'},
    12: {'name': 'kabir', 'age': 35, 'email': 'kabir61@yahoo.com'},
    13: {'name': 'anjali', 'age': 32, 'email': 'anjali67@gmail.com'},
    14: {'name': 'suresh', 'age': 26, 'email': 'suresh88@icloud.com'},
    15: {'name': 'siddharth', 'age': 30, 'email': 'siddharth68@gmail.com'},
    16: {'name': 'meera', 'age': 22, 'email': 'meera51@gmail.com'},
    17: {'name': 'tanya', 'age': 31, 'email': 'tanya38@outlook.com'},
    18: {'name': 'tanya', 'age': 24, 'email': 'tanya33@icloud.com'},
    19: {'name': 'rohan', 'age': 35, 'email': 'rohan23@gmail.com'},
    20: {'name': 'anjali', 'age': 26, 'email': 'anjali23@yahoo.com'},
    21: {'name': 'karan', 'age': 35, 'email': 'karan45@icloud.com'},
    22: {'name': 'ritesh', 'age': 23, 'email': 'ritesh76@yahoo.com'},
    23: {'name': 'siddharth', 'age': 25, 'email': 'siddharth81@gmail.com'},
    24: {'name': 'sneha', 'age': 21, 'email': 'sneha35@icloud.com'},
    25: {'name': 'meera', 'age': 33, 'email': 'meera58@icloud.com'},
    26: {'name': 'ritesh', 'age': 33, 'email': 'ritesh79@outlook.com'},
    27: {'name': 'aryan', 'age': 35, 'email': 'aryan73@outlook.com'},
    28: {'name': 'anjali', 'age': 24, 'email': 'anjali52@gmail.com'},
    29: {'name': 'meera', 'age': 26, 'email': 'meera79@yahoo.com'},
    30: {'name': 'vikram', 'age': 28, 'email': 'vikram53@icloud.com'},
    31: {'name': 'vikram', 'age': 34, 'email': 'vikram59@outlook.com'},
    32: {'name': 'priya', 'age': 34, 'email': 'priya21@outlook.com'},
    33: {'name': 'aryan', 'age': 32, 'email': 'aryan44@gmail.com'},
    34: {'name': 'aryan', 'age': 19, 'email': 'aryan30@outlook.com'},
    35: {'name': 'sneha', 'age': 21, 'email': 'sneha31@outlook.com'},
    36: {'name': 'siddharth', 'age': 33, 'email': 'siddharth31@gmail.com'},
    37: {'name': 'meera', 'age': 20, 'email': 'meera75@yahoo.com'},
    38: {'name': 'rohan', 'age': 29, 'email': 'rohan64@outlook.com'},
    39: {'name': 'ritesh', 'age': 19, 'email': 'ritesh33@outlook.com'},
    40: {'name': 'siddharth', 'age': 23, 'email': 'siddharth34@outlook.com'},
    41: {'name': 'siddharth', 'age': 25, 'email': 'siddharth90@outlook.com'},
    42: {'name': 'sneha', 'age': 22, 'email': 'sneha38@icloud.com'},
    43: {'name': 'vikram', 'age': 25, 'email': 'vikram42@outlook.com'},
    44: {'name': 'priya', 'age': 20, 'email': 'priya37@icloud.com'},
    45: {'name': 'priya', 'age': 21, 'email': 'priya86@outlook.com'},
    46: {'name': 'rohan', 'age': 35, 'email': 'rohan42@icloud.com'},
    47: {'name': 'ritesh', 'age': 23, 'email': 'ritesh32@gmail.com'},
    48: {'name': 'sneha', 'age': 34, 'email': 'sneha61@outlook.com'},
    49: {'name': 'kabir', 'age': 34, 'email': 'kabir35@gmail.com'},
    50: {'name': 'tanya', 'age': 23, 'email': 'tanya67@icloud.com'}
}


#get all data / or with limits
@app.get("/post") #post?limit=for eg 10
def get_posts():
    
    return text_posts #it shoud be pydantic objec or python dictinary

#JSON  fromatte is the formatt to  dealing data across web so that why it is necessary to return y dictonay or pydantic ibj


#Query Parameter 
@app.get("/lim-post/")
def get_limited_Posts(limit:int):
    if limit > len(text_posts.keys()):
        raise HTTPException(status_code=404,detail="Limit should be lower than data size")
    return list(text_posts.values())[:limit]


#get specific for a  id
@app.get("/post/{post_id}")
def get_post_as_id(post_id:int)-> PostResponse:
    if post_id not in text_posts:
        raise HTTPException(status_code=404,detail="Post not found") #raises error if id not found
    return text_posts.get(post_id)

#create post
@app.post("/posts")
def create_post(post:PostCreate)->PostResponse:
    new_post={"name":post.name,"age":post.age,"email":post.email}
    text_posts[max(text_posts.keys())+1]=new_post
    return new_post

#delete specific data
@app.delete("/delete/{post_id}")
def delete_post(post_id:int):
    print(f"deleted record {text_posts.get(post_id)}")
  
    text_posts.pop(post_id,None)

#update all field of that row
@app.put("/put_post/{post_id}")
def put_post(post_id: int, post: PostCreate) -> PostResponse:
   if post_id not in text_posts.keys():
        raise HTTPException(status_code=404,detail="Post not found")
   text_posts[post_id] = post.model_dump()

   return text_posts[post_id]

#patch
@app.patch("/posts/patch/{post_id}")
def patch_post(post_id: int,post:PostPatch):
    if post_id not in text_posts.keys():
        raise HTTPException(status_code=404,detail="Post not found")
    
    existing_post=text_posts[post_id]
    update_data = post.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        existing_post[key] = value  
    return existing_post