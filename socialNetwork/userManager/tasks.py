from socialNetwork.celery import app
import logging
import time

logger = logging.getLogger(__name__)


@app.task(name='buc')
def buc(user_id):
    i = 0
    while True:
        logger.warning(f"Identifier: {user_id} taskID: {buc.request.id} -- {i}")
        time.sleep(1)
        i += 1
