#Python
from uuid import UUID #Identidicadores
from datetime import date
from datetime import datetime
from typing import Optional, List

#Pydantic
from pydantic import Field
from pydantic import BaseModel, EmailStr


#FastAPI
from fastapi import FastAPI
from fastapi import status


app = FastAPI()


#Models
class UserBase(BaseModel):
    user_id: UUID = Field(...) #Identificador unico
    email: EmailStr =Field(...)


class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length = 8,
        max_length = 64    
    ) 

class User(UserBase):
    
    first_name: str =Field(
        ...,
        min_length = 1,
        max_length = 50
    )
    birth_date: Optional[date] = Field(default=None) #Campo opcional a ingresar

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length = 1,
        max_length = 256
    )
    create_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)
#Path operations


###Users
@app.post(
    path="/signup",
    response_model=User, 
    status_code=status.HTTP_201_CREATED,
    summary="Register a user",
    tags=["Users"]
)

def signup():
    pass
###Login
@app.post(
    path="/login",
    response_model=User, 
    status_code=status.HTTP_200_OK,
    summary="Login a user",
    tags=["Users"]
)

def login():
    pass

###Show_all_users
@app.get(
    path="/users",
    response_model=List[User], 
    status_code=status.HTTP_200_OK,
    summary="show all user",
    tags=["Users"]
)

def show_all_users():
    pass


###show_a_user
@app.get(
    path="/users/{user_id}",
    response_model=User, 
    status_code=status.HTTP_200_OK,
    summary="show a user",
    tags=["Users"]
)

def show_a_user():
    pass

###Delete users
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User, 
    status_code=status.HTTP_200_OK,
    summary="delete a user",
    tags=["Users"]
)

def delete_a_user():
    pass


###Update users
@app.put(
    path="/users/{user_id}/update",
    response_model=User, 
    status_code=status.HTTP_200_OK,
    summary="update a user",
    tags=["Users"]
)

def update_a_user():
    pass

#Tweets

###Show all tweets
@app.get(
    path="/",
    response_model=List[Tweet], 
    status_code=status.HTTP_200_OK,
    summary="Show all Tweets",
    tags=["Tweets"]

)
def home():
    return {"Twiter API": "Working!"}

##Post a tweets
@app.post(
    path="/post",
    response_model=Tweet, 
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
)

def post():
    pass

###Show a tweets
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet, 
    status_code=status.HTTP_200_OK,
    summary="show a tweet",
    tags=["Tweets"]
)

def show_a_tweet():
    pass
###Delete a tweet
@app.post(
    path="/tweets/{tweets_id}/delete",
    response_model=Tweet, 
    status_code=status.HTTP_200_OK,
    summary="delete a tweet",
    tags=["Tweets"]
)

def delete_a_tweet():
    pass

###Update a tweet
@app.put(
    path="/tweets/{tweets_id}/update",
    response_model=Tweet, 
    status_code=status.HTTP_200_OK,
    summary="update a tweet",
    tags=["Tweets"]
)

def update_a_tweet():
    pass