from fastapi import FastAPI

app = FastAPI()


@app.get("/api-endpoint")
async def root():
    return {"message": "Hello Marshal"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
