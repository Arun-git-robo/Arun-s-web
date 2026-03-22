import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

HTML = open("index.html", "r").read()

@app.get("/", response_class=HTMLResponse)
async def root():
    return HTMLResponse(content=HTML)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
