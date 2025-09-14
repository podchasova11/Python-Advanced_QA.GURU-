from datetime import datetime, timezone


users = {
        5: {
            "id": 5,
            "email": "charles.morris@reqres.in",
            "first_name": "Charles",
            "last_name": "Morris",
            "avatar": "https://reqres.in/img/faces/5-image.jpg"
        },

        7: {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"

        }
    }

create_user = {
    "name": "morpheus",
    "job": "leader"
}

update_user = {
    "name": "lawrence",
    "job": "actor"
}

register_user = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

login_user = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}


support_info = {
        "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
        "text": "Tired of writing endless social media content? Let Content Caddy generate it for you.",
    }

timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")

non_exist_id = 79

