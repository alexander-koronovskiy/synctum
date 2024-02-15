from fastapi import FastAPI, Body
from router import add_spin, show_statistics

app = FastAPI()


@app.get("/")
def read_root():
    return {"route statistics": show_statistics()}


@app.post("/add_route/")
async def add_route(data=Body()):
    user_id, route = data['user_id'], data['route']
    add_spin(user_id, route)
