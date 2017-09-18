
from django.conf.urls import url
from . import views

from .view import profile, offer

urlpatterns = [

    url(r'^$', views.Home),
    url(r'login', views.loginV),
    url(r'logout', views.logoutV),

    url(r'offers$', offer.lister),
    url(r'offers/new$', offer.new),
    url(r'offers/(?P<pk>\d+)/$', offer.get),

    #Profile views
    url(r'profiles$', profile.lister),
    url(r'profiles/new$', profile.new),
    url(r'profiles/(?P<pk>\d+)/$', profile.get),

    url(r'interests', views.interests),
    url(r'reports', views.reports),
    url(r'groups', views.groups),
    url(r'contact', views.contact),

]
