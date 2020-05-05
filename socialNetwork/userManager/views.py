from django.shortcuts import render, HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info(f"Function: {index.__name__} prints hello world")
    return HttpResponse("Hola")
