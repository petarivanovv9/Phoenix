from django.conf.urls import url

from .views import (index, log_in, register, log_out)


urlpatterns = [
    #'',
    url(r'^$', index, name='index'),
    url(r'^login/$', log_in, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', log_out, name='logout'),
]
