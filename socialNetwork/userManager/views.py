from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import logging


logger = logging.getLogger(__name__)


def index(request):
    if not request.user.is_authenticated:
        message = "Not authenticated"
    else:
        message = f"Authenticated with {request.user}"
    return HttpResponse(message)  # render(request, "users/user.html", context)


def add_user(request):
    if request.user.is_authenticated:
        logger.info(f"Logging attempt with an already authenticated user\n\tUser: {request.user}")
        return HttpResponseRedirect(reverse("index"))

    return render(request, 'userManager/sign_up.html')


# TODO: remove the csrf_exempt
@csrf_exempt
def login_view(request):
    if request.user.is_authenticated:
        logger.info(f"Logging attempt with an already authenticated user: {request.user}")
        return HttpResponseRedirect(reverse("index"))

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        logger.info(f"Logging attempt for: {username}")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            logger.info(f"Logged successfully")
            return HttpResponseRedirect(reverse("index"))
        else:
            logger.info(f"Invalid credentials")
            return render(request, "userManager/login.html", {"message": "Invalid credentials, try again."}, status=401)

    return render(request, "userManager/login.html", {"message": None})


def logout_view(request):
    logger.info(f"Logout attempt for: {request.user}")
    logout(request)
    return render(request, "userManager/login.html", {"message": "Logged out."})


# TODO: remove the csrf_exempt
@csrf_exempt
def add_user_service(request):
    logger.info(f"Ajax: {request.is_ajax()}")
    # Only allowed if is Ajax and method is POST
    if request.method == 'POST' and request.is_ajax():
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        logger.debug(f"User Info:\n\tUsername: {username}\n\tEmail: {email}\n\tPassword: {password}")
        if User.objects.filter(email=email).exists():
            logger.error(f"Email is already taken")
            # Code 409 Conflict
            return JsonResponse({"error": "This email is already registered"}, status=409)

        try:
            user = User.objects.create_user(username=username, email=email, password=password,
                                            first_name=first_name, last_name=last_name)
            user.save()
            logger.debug(f"User saved!")
            return JsonResponse({"message": " User saved"}, status=200)

        except IntegrityError as e:
            logger.error(f"User already exist \n\tERROR: {e}")
            # Code 409 Conflict
            return JsonResponse({"error": "Username is already taken"}, status=409)

    else:
        logger.info(f"Method not allowed: isAjax() = {request.is_ajax()} method = {request.method}")
        return JsonResponse({"error": "Method not allowed"}, status=405)
