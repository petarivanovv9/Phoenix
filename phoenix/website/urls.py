from django.conf.urls import url

from .views import (index, log_in, register)


urlpatterns = [
    #'',
    url(r'^$', index, name='index'),
    url(r'^login/$', log_in, name='login'),
    url(r'^register/$', register, name='register'),
]
