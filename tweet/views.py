from django.shortcuts import render
from .models import Tweet
# Create your views here.

def home(request):
    tweets = Tweet.objects.all()
    return render(request,'public/index.html',{'tweets':tweets})