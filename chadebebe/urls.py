
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

from django.urls import include, path




urlpatterns = [
    path('', Homecha ,name='homecha'),

]