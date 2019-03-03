from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    word_list = ['1', '2', '3']
    return render(request, 'index.html',
                  {"index_title": "django_test website",
                   "word_list": word_list})


def user_detail(request, user_id):
    return HttpResponse('This  is number {} user details'.format(user_id))
