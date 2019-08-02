from django.conf.urls import url, include
from .views import landing_page, create_issue, view_issue, edit_issue

urlpatterns = [
    url(r'^$', landing_page, name='index'),
    url(r'^create_issue/$', create_issue, name='create_issue'),
    url(r'^(?P<pk>\d+)/$', view_issue, name='view_issue'),
    url(r'^(?P<pk>\d+)/edit_issue/$', edit_issue, name='edit_issue'),
]