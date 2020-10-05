from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return f"{self.user} liked {self.tweet}"
    

class Tweet(models.Model):

    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tweets")
    content = models.CharField(max_length=250)
    likes = models.ManyToManyField(User,related_name='tweet_user', blank=True, through=TweetLike)
    # image = models.ImageField(upload_to=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.content}- By {self.user.first_name} {self.user.last_name}"

    def tweet_likes(self):
        return self.likes.count()


    class Meta:
        ordering = ("-updated_at",)



# class Follower(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='USER')
#     follower = models.ManyToManyField(settings.AUTH_USER_MODEL)
#     timestamp = models.DateTimeField(auto_now_add=True)
    