import pytest

PROD = "https://reqres.in" 
TEST = "http://127.0.0.1:8000"

USERS_API = "/api/users"  
REGISTER_API = "/api/register"
LOGIN_API = "/api/login"


@pytest.fixture(params=[PROD, TEST])
def domain_url(request):
    return request.param


@pytest.fixture()
def base_endpoint(domain_url):
    base_endpoint = f"{domain_url}{USERS_API}"
    register_endpoint = f"{domain_url}{REGISTER_API}"
    login_endpoint = f"{domain_url}{LOGIN_API}"
    return base_endpoint, register_endpoint, login_endpoint
