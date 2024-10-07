"""
URL configuration for home project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
#path: E:\Koodi\DJANGO\Calendar\home\home\urls.py
# Path: E:\Koodi\DJANGO\Calendar\home\home\urls.py
from django.contrib import admin
from django.urls import path
from databasemgnt.views import add_event, poistaevent
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('add_event/', add_event, name='add_event'),
    path('poistaevent/<int:id>/', poistaevent, name='poistaevent'),
]
