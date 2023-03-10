
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        path('login/', auth_views.LoginView.as_view(template_name = 'form.html',), name ='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),

]
