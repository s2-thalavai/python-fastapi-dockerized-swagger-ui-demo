from fastapi import FastAPI

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})

@app.get("/", summary="First FastAPI example")
async def my_first_get_api():
    return {"message":"First FastAPI example"}


@app.get("/users/{username}")
async def read_user(username: str):
    return {"message": f"Hello {username}"}