from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from .views import *

from django.shortcuts import redirect

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'issues', IssueViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'relatedlinks', RelatedLinkViewSet)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', indexview),
    url(r'^ddapi/', include(router.urls)),
    # url(r'^$', 'directdemocracy.views.home', name='home'),
    # url(r'^directdemocracy/', include('directdemocracy.foo.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
    #url(r'^.*$', indexview),
    url(r'^[^s][^t][^a][^t][^i][^c]', indexview),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
