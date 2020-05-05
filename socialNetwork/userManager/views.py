from django.shortcuts import HttpResponse, render
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)


@csrf_exempt
def index(request):
    logger.info(f"[FUNCTION: {index.__name__}] [METHOD: {request.method}] [Ajax: {request.is_ajax()}]")
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        logger.debug(f"[{index.__name__}] \n\tUsername: {username}\n\tEmail: {email}\n\tPassword: {password}")
        try:
            user = User.objects.create_user(username=username, email=email, password=password,
                                            first_name=first_name, last_name=last_name)
            user.save()
            logger.debug(f"[{index.__name__}] User saved!")
            return JsonResponse({"message": " User saved!"}, status=200)
        except IntegrityError as e:
            logger.error(f"[{index.__name__}] User already exist \n\tERROR: {e}")
            return JsonResponse({"error": "User already exist"}, status=400)

    return render(request, 'userManager/index.html')

