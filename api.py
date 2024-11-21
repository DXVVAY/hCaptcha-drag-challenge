from fastapi import FastAPI, Request
from pydantic import BaseModel
from solver import DragDrop
from utils import log
import logging, time

logging.getLogger("uvicorn.access").disabled = True

class Data(BaseModel):
    captcha: dict

class API:
    def __init__(self) -> None:
        self.app: FastAPI = FastAPI()
        self.app.post("/solve")(self.solve)
    
    def solve(self, data: Data, request: Request) -> dict:
        start = time.time()   
        result = DragDrop(data.captcha, verbose=False).solve()
        coords = [entity["entity_coords"] for entity in list(result.values())[0]]
        log.info(f"IP -> {request.client.host} | Result -> {coords}...", level="Solved", start=start, end=time.time())
        return {
            "result": result,
            "took": f'{(time.time() - start) * 1000}ms'
        }

app = API().app