from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.


def index(request):
    word_list = ['1', '2', '3']
    word_list = Post.objects.all().order_by('-publish_date')
    return render(request, 'index.html',
                  {"index_title": "django_test website",
                   "word_list": word_list})


def user_detail(request, user_id):
    return HttpResponse('This  is number {} user details'.format(user_id))
