
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Home),
    url(r'login', views.loginV),
    url(r'logout', views.logoutV),
    url(r'offers', views.offers),
    url(r'interests', views.interests),
    url(r'reports', views.reports),
    url(r'groups', views.groups),
    url(r'contact', views.contact),

]
