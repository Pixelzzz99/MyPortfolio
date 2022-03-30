from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user

from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
# from rest_framework import status_code

from .forms import EditProfileForm, CreateProjectForm

from info.models import Information, Message, Project, Education

from .serializers import *


class LoginView(APIView):
    pass


def dashboard(request):
    if request.method == 'GET':
        pass


def profile(request):
    pass


def profile_edit(request):
    pass


def messages(request):
    pass


def messages_api(request):
    pass


def projects(request):
    pass


def projects_api(request):
    pass


class EducationView(APIView):
    pass
