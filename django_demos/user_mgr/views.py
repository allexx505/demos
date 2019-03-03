from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Welcome to the user manager!!!!!')

def user_detail(request, user_id):
    return HttpResponse('This is number {} user details'.format(user_id))