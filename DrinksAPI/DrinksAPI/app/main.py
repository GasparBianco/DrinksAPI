from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def helloWorld():
    return "hello world"

