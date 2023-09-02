from typing import Union

from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
from  configparser import ConfigParser
 
import logging
import datetime
import logging.config
import logging.handlers
 
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

################################################################################################
# main appliction                                                                              #
################################################################################################
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=4000)
    #uvicorn.run("app:app", log_level="info")