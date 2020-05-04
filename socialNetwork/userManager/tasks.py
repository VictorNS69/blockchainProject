from socialNetwork.celery import app
import logging
import time

logger = logging.getLogger(__name__)


@app.task(name='prueba_suma')
def prueba_suma(x, y):
    logger.info("Esto sale por celery")
    logger.info(f"El valor de {x} + {y} es {x + y}")
    return x + y


@app.task(name='buc')
def buc():
    i = 0
    while True:
        logger.warning(f"id: {buc.request.id} -- {i}")
        time.sleep(1)
        i += 1
