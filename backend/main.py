from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def first_example():
    return {"message": "Hello, FastAPI!"}