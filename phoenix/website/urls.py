from django.conf.urls import url

from .views import (index, login, register)


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^register/$', register, name='register'),
]
