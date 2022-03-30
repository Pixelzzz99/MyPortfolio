from django.urls import path
from django.contrib.auth.views import LogoutView
from django.urls import include

from .views import (
    dashboard,
    profile,
    profile_edit,
    messages,
    messages_api,
    projects,
    projects_api,
    LoginView,
    EducationView
)

from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets


router = routers.DefaultRouter()
router.register(r'dashboard', dashboard, 'dashboard')
router.register(r'profile', profile, 'profile')
router.register(r'profile_edit', profile_edit, 'profile_edit')
router.register(r'message', messages, 'messages')
router.register(r'messages_api', messages_api, 'messages_api')
router.register(r'projects', projects, 'projects')
router.register(r'projects_api', projects_api, 'projects_api')
router.register(r'login', LoginView, 'login')
router.register(r'education', EducationView, 'Education')


urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls')),
]

