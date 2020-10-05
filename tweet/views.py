from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Tweet,TweetLike
from django.contrib.auth.decorators import login_required
from django.contrib import messages

class TweetList(ListView):
    model = Tweet
    template_name = 'public/index.html'
    context_object_name = 'tweets'

@login_required
def create_tweet(request):
    if request.method == 'POST':
        content = request.POST['content']
        if content == "":
            messages.warning(request, "Tweet Cannot Be Blank. ")
            return redirect('/')
        new_tweet = Tweet(user = request.user, content=content)
        new_tweet.save()
        return redirect('/')



def tweet_like(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    is_liked = TweetLike.objects.filter(tweet=tweet,user=request.user).exists()
    if not is_liked:
        tweet.likes.add(request.user)
        is_liked = False
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def tweet_dislike(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    is_liked = TweetLike.objects.filter(tweet=tweet,user=request.user).exists()
    if is_liked:
        tweet.likes.remove(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

