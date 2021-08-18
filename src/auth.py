from flask import Blueprint

auth = Blueprint("bo", __name__, url_prefix="/api/v1/auth")


@auth.post("/register")
def register():
    return "User"


@auth.get("/me")
def me():
    return {"user": "me"}
