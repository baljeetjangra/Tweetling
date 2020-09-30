
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Tweetling Admin Panel"
admin.site.site_title = "Tweetling"
admin.site.index_title = "Welcome to the Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('tweet.urls')),
]
