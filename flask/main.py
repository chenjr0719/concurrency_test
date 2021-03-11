import logging
import time
from datetime import datetime

from flask import Flask, request

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

app = Flask("test")

@app.route("/", methods=["GET", "POST"])
def test():
    logger.debug(f"requst at {datetime.now().isoformat()}")

    request_data = request.get_json()
    logger.debug({"request": request_data})

    time.sleep(2)
    message = {"message": "Hello World"}
    logger.debug(f"resp at {datetime.now().isoformat()}")
    return message

if __name__ == "__main__":
    # import bjoern
    # bjoern.run(app, "0.0.0.0", 8000, reuse_port=True)
    app.run(host="0.0.0.0", port=8000)
