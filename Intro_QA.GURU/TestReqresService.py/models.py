from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: str
    password: str


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class SupportInfo(BaseModel):
    url: str
    text: str


class SuccessRegisterData(BaseModel):
    id: int
    token: str


class SuccessLoginData(BaseModel):
    token: str


class CreateUserRequest(BaseModel):
    name: str
    job: str


class CreatedUserData(BaseModel):
    name: str
    job: str
    id: int
    createdAt: str


class UpdatedUserData(BaseModel):
    name: str
    job: str
    updatedAt: str


class ResponseModel(BaseModel):
    data: UserData
    support: SupportInfo
  
