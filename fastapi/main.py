import logging
import asyncio
from datetime import datetime
import time
from fastapi import FastAPI, Request

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

app = FastAPI()


@app.api_route("/", methods=["GET", "POST"])
async def root(request: Request):
    logger.debug(f"requst at {datetime.now().isoformat()}")

    request_data = await request.body()
    logger.debug({"request": request_data})

    await asyncio.sleep(2)
    # time.sleep(2)
    message = {"message": "Hello World"}
    logger.debug(f"resp at {datetime.now().isoformat()}")

    return message

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
