
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Tweetling Admin Panel"
admin.site.site_title = "Tweetling"
admin.site.index_title = "Welcome to the Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('tweet.urls')),
    path('accounts/',include('accounts.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)