import data
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from models import ResponseModel, CreatedUserData, SuccessRegisterData, UpdatedUserData, User, CreateUserRequest, \
    SuccessLoginData
from random import randint

app = FastAPI()


@app.get("/api/users/{user_id}", response_model=ResponseModel)
def get_user(user_id: int) -> ResponseModel | JSONResponse:
    users = data.users
    support_info = data.support_info

    user = users.get(user_id)
    if not user:
        return JSONResponse(
            status_code=404, content={}
        )

    return ResponseModel(data=user, support=support_info)


@app.post("/api/users", response_model=CreatedUserData, status_code=201)
def create_user(request_data: CreateUserRequest) -> CreatedUserData:
    new_id = randint(100, 250)
    date = data.timestamp

    return CreatedUserData(
        name=request_data.name,
        job=request_data.job,
        id=new_id,
        createdAt=date
    )


@app.post("/api/register", response_model=SuccessRegisterData)
def register_user(user: User) -> SuccessRegisterData | JSONResponse:
    if user.email == data.register_user['email'] and user.password == data.register_user['password']:
        return SuccessRegisterData(id=4, token="QpwL5tke4Pnpja7X4")

    if not user.email:
        return JSONResponse(
            status_code=400,
            content={"error": "Missing email or username"}
        )

    if not user.password:
        return JSONResponse(
            status_code=400,
            content={"error": "Missing password"}
        )

    else:
        return JSONResponse(
            status_code=400,
            content={ "error": "Note: Only defined users succeed registration"}
        )


@app.post("/api/register", response_model=SuccessLoginData)
def register_user(user: User) -> SuccessLoginData | JSONResponse:
    if user.email == data.register_user['email'] and user.password == data.register_user['password']:
        return SuccessLoginData(id=4, token="QpwL5tke4Pnpja7X4")

    if not user.email:
        return JSONResponse(
            status_code=400,
            content={"error": "Missing email or username"}
        )

    if not user.password:
        return JSONResponse(
            status_code=400,
            content={"error": "Missing password"}
        )

    else:
        return JSONResponse(
            status_code=400,
            content={"error": "Note: Only defined users succeed login"}
        )


@app.put("/api/users/{user_id}", response_model=UpdatedUserData)
def update_user(user_id: int, req_data: CreateUserRequest) -> UpdatedUserData | JSONResponse:
    user_ids = [5, 7]
    date = data.timestamp
    if user_id not in user_ids:
        return JSONResponse(
            status_code=400,
            content={"error": "User ID does not exist"}
        )
    else:
        return UpdatedUserData(name=req_data.name, job=req_data.job, updatedAt=date)


@app.delete("/api/users/{user_id}")
def delete_user() -> Response:
    return Response(status_code=204)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
  
