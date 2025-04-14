from django.urls import path
import users.views

app_name = "users"

urlpatterns = [
    path('', users.views.index, name='index'),
    path('register/', users.views.register, name='register'),
    path('login/', users.views.login, name='login'),
    path('protected/', users.views.protected_route, name='protected'),
]