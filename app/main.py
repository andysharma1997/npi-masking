"""This is the main module to start the service
This module defines below usecases:
1) Configures logger
4) Creates multiple middlewares
5) Api versioning
6) Including routers
"""

__version__ = "v1.0"
__author__ = "shubham@salesken.ai"


from fastapi import FastAPI, Request
from app.utilities import sken_logger
from app.routers import index


logger = sken_logger.get_logger(__name__)

app = FastAPI()

@app.get("/")
async def healthcheck():
    return {"status": "alive"}

subapi =  FastAPI()
subapi.include_router(index.router)

app.mount("/v1/anonymize",subapi)

logger.info("Main application initialized")

if __name__ == "__main__":
    pass