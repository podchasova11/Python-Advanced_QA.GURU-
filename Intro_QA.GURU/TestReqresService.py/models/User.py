# 1. Разработать несколько API-автотестов на https://reqres.in (если обучались на основном курсе python - можно взять код автотестов из домашнего задания)

# Можно также за основу взять https://github.com/qa-guru/qa_guru_python_9_19



# 2. Вместо https://reqres.in разработать свой микросервис в стеке Python + FastAPI (допускается также Flask, Django).

# Пример - https://github.com/qa-guru/python-advanced-intro, https://github.com/qa-guru/reqres-service

# - Автотесты должны также успешно проходить.

# - В коде микросервиса не должно быть хардкода.

# Например, не должно быть эндпоинтов типа /api/users/2 - правильнее /api/users/{user_id}


from pydantic import BaseModel, EmailStr, HttpUrl


class User(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    avatar: HttpUrl
