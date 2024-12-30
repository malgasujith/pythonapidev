from pydantic import BaseModel

class Datamodel(BaseModel):
    username : str
    password:  str
    email:     str
    mobile:    str
    role:      str


class jwtdatamodel(BaseModel):
    username: str
    role: str
    expire: int
