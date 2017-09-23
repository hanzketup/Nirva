
from django.conf.urls import url
from . import views

from .view import profile, offer, interests, group

urlpatterns = [

    url(r'^$', views.Home),
    url(r'login', views.loginV),
    url(r'logout', views.logoutV),

    #dispatcher
    url(r'dispatcher$', views.dispatch),
    url(r'log$', views.log),

    #offer views
    url(r'offers$', offer.lister),
    url(r'offers/new$', offer.new),
    url(r'offers/(?P<pk>\d+)/$', offer.get),
    url(r'offers/(?P<pk>\d+)/save$', offer.save),
    url(r'offers/(?P<pk>\d+)/remove', offer.remove),

    #Profile views
    url(r'profiles$', profile.lister),
    url(r'profiles/new$', profile.new),
    url(r'profiles/(?P<pk>\d+)/$', profile.get),

    #Interests views
    url(r'interests$', interests.lister),
    url(r'interests/new$', interests.new),
    url(r'interests/(?P<pk>\d+)/$', interests.get),
    url(r'interests/(?P<pk>\d+)/remove$', interests.remove),

    #groups views
    url(r'groups$', group.lister),
    url(r'groups/new$', group.new),
    url(r'groups/(?P<pk>\d+)/$', group.get),
    url(r'groups/(?P<pk>\d+)/remove$', group.remove),
    url(r'groups/(?P<pk>\d+)/save$', group.save),

    #mock
    url(r'^mock$', views.mock),

]
