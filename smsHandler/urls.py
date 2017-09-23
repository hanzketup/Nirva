
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.smsIn),
    url(r'^mock', views.mockIn),

]
