from django.shortcuts import render, HttpResponse
from .tasks import prueba_suma, buc
from celery.task.control import revoke
import logging


logger = logging.getLogger(__name__)

id_task = 0
# Create your views here.
def index(request):
    resultado = prueba_suma.delay(5, 6)
    id_task = buc.delay()
    logger.info(f"El resultado es: {resultado}")
    logger.info(f"ID_task es: {id_task}")
    logger.info("Test de log")
    return HttpResponse("Hola ")

def stop(request, id):
    logger.info(f"Parando {id}")
    revoke(id, terminate=True, signal='SIGKILL')
    return HttpResponse("Stop!")