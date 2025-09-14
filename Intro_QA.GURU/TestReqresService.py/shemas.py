post_users = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "id": {
            "type": "string"
        },
        "createdAt": {
            "type": "string"
        },
        "job": {
            "type": "string"
        },
        "name": {
            "type": "string"
        }
    },
    "required": [
        "id",
        "createdAt",
        "job",
        "name"
    ]
}

post_login_success = {

    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "token": {
            "type": "string",
            "minLength": 1
        }
    },
    "required": ["token"],
    "additionalProperties": False
}
