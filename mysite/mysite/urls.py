from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^budgest/', include('budgest.urls', namespace='budgest')),
    url(r'^admin/', include(admin.site.urls)),
]
