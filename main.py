from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/message")
def message(id:str, message:str):
    return {"id": id, "message": message+f" from id: {id}."}
