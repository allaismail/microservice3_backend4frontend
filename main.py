import fastapi as _fastapi
import requests
import json
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from config import settings

app = _fastapi.FastAPI()
class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    profession: str

app.add_middleware(
CORSMiddleware,
allow_origins=["*"], # Allows all origins
allow_credentials=True,
allow_methods=["*"], # Allows all methods
allow_headers=["*"], # Allows all headers
)

url1="http://"+settings.IP_M1+":"+settings.PORT_M1+"/users/"
url2="http://"+settings.IP_M2+":"+settings.PORT_M2+"/users/"


@app.get("/user/{id}")
async def get_user(id : int):
    rep1=requests.get(url1+str(id))
    rep1=rep1.json()
    rep2=requests.get(url2+str(id))
    rep2=rep2.json()
    
    return {  "id":id,
              "first_name":rep1['first_name'],
              "last_name":rep1['last_name'],
              "profession": rep2['profession'] }


@app.post("/user/")
async def create_item(user: User):
    user1={"id":user.id,"first_name":user.first_name,"last_name":user.last_name}
    user2={"id":user.id,"profession":user.profession}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r1 = requests.post(url1, data=json.dumps(user1), headers=headers)
    r2 = requests.post(url2, data=json.dumps(user2), headers=headers)
    return user




