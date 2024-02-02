"""
URL configuration for yourprojectname project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# Gunicorn Static file Settings
from django.conf import settings
from django.conf.urls.static import static
from auth_app.models import homemodel
from django.utils.crypto import get_random_string

### home page login
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from enum import unique
from django.shortcuts import redirect,render
from rest_framework import generics, permissions


def token():
    unique_id = get_random_string(length=32)
    return unique_id


token=token()

def login(request,token=token):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        password = request.POST.get('password')
        print(password)
        user = homemodel.objects.get(Username = name)
        passcode = user.password
        print(passcode)
        if passcode==password:
            return redirect('swagger/'+token)
        else:
            return render(request,'login.html',{"message":"please login with correct credentials"})
    return render(request,'login.html')

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('yourappname.urls')),
    path('apiconsole',include('auth_app.urls')),
    path('',login),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/'+token, schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),


]

# Add the following lines for serving static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
