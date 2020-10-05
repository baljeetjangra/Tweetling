from django.urls import path
from .views import TweetList,create_tweet, tweet_like, tweet_dislike


urlpatterns = [
    path('',TweetList.as_view(), name='home'),
    path('createtweet/',create_tweet, name='create_tweet'),
    path('tweetlike/<int:tweet_id>/',tweet_like, name='tweet_like'),
    path('tweetdislike/<int:tweet_id>/',tweet_dislike, name='tweet_dislike'),
]
