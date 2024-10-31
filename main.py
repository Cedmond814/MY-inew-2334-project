from fastapi import FastAPI

app = FastAPI()

@app.get("/api/welcome")
def welcome():
    return {"message": "Welcome to the FastAPI REST service!"}
