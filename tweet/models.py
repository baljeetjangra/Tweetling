from django.db import models
from django.conf import settings
# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tweet = models.CharField(max_length=250)
    # image = models.ImageField(upload_to=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tweet}- By {self.user.first_name} {self.user.last_name}"

