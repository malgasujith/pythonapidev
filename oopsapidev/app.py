from fastapi import FastAPI, Request,Header
import uvicorn
from db_server import  Dbsc
from Health import Health
from registration import  reg_service
from pydantic1 import Datamodel,jwtdatamodel
from jwttoken import Jwttoken
from authentication import Auth_token


host = "spring2.ctc8eosquvzt.eu-north-1.rds.amazonaws.com"
dbname = "edwin"
user = "postgres"
password = "sujith123"


app = FastAPI()

obj1 = Dbsc(host,dbname,user,password)
obj1.user_schema()
o_jwt = Jwttoken(host,dbname,user,password)
O_AUTH = Auth_token(host,dbname,user,password)

@app.get('/health')
def health_check():
    obj_health = Health()
    return obj_health.health_ch()


@app.post("/regestration")
async def regestration(body: Datamodel ):
    obj1_reg = reg_service(host, dbname, user, password)
    respond = obj1_reg.user_registration(body.dict())
    return respond

@app.post("/create/token")
async def create(body: jwtdatamodel,request: Request):
        js_body1 = await request.json()
        respond = o_jwt.creat_token(js_body1)
        return respond


@app.get("/users")
def userslist(authorization: str = Header(...)):
    token = authorization.split(" ")[1] 
    response = O_AUTH.get_user(token)
    return response

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)


    # "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InJhbXlhIiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNzM3OTY5NzQ4LjE3NjY0fQ.Wwl5dIMl4VfPyIUV6c7DKM3qjpvCTBzt_VUNgiLMuvU"
    # Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InJhbXlhIiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNzQwNTY0ODg5LjI1NjkxOX0.brfGQ9000Csote5_K0xq_B2vt8nHSltYPMyGjlCTz8Q
    # "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InN1aml0aCIsInJvbGUiOiJhZG1pbiIsImV4cCI6MTc0MDcxNzMzNC41MjY0MDh9.hsiJjM-5RxSKyDHPqRI3NIEC-7BEEDEeHsPosYVjFu0"
