import django.http
import django.views.decorators.csrf
import django.views.decorators.http

from users.models import Users
import users.forms
from users.utils import generate_jwt, decode_jwt

@django.views.decorators.csrf.csrf_exempt
@django.views.decorators.http.require_POST
def register(request):
    data = request.POST

    form = users.forms.RegisterForm(data)

    if form.is_valid():
        query = Users.objects.create(
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password'),
            email=form.cleaned_data.get('email'),
            name=form.cleaned_data.get('name')
        )
        token = generate_jwt(query)
        return django.http.JsonResponse({"token": token}, status=200)
    else:
        return django.http.JsonResponse({"error": form.errors}, status=400)


@django.views.decorators.csrf.csrf_exempt
@django.views.decorators.http.require_POST
def login(request):
    data = request.POST

    form = users.forms.LoginForm(data)

    if form.is_valid():
        user = Users.objects.filter(username=form.cleaned_data.get('username')).first()
        token = generate_jwt(user)
        return django.http.JsonResponse({"token": token}, status=200)
    else:
        return django.http.JsonResponse({"error": form.errors}, status=400)

def index(request):
    return django.http.JsonResponse({"message": "Successful"}, status=200)

def protected_route(request):
    # Check for Authorization header
    auth_header = request.headers.get('Authorization')
    
    if not auth_header or not auth_header.startswith('Bearer '):
        return django.http.JsonResponse({"error": "No token provided"}, status=401)
    
    # Extract the token
    token = auth_header.split(' ')[1]
    
    # Decode and verify token
    payload = decode_jwt(token)
    
    if not payload:
        return django.http.JsonResponse({"error": "Invalid or expired token"}, status=401)
    
    # Get user from payload
    user_id = payload.get('id')
    user = Users.objects.filter(id=user_id).first()
    
    if not user:
        return django.http.JsonResponse({"error": "User not found"}, status=404)
    
    # Return protected data
    return django.http.JsonResponse({
        "message": "You accessed a protected route",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "name": user.name
        }
    }, status=200)
    
