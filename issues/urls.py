from django.conf.urls import url, include
from .views import landing_page, create_issue, view_issue, edit_issue, upvote_issue, delete_issue, create_comment

urlpatterns = [
    url(r'^$', landing_page, name='index'),
    url(r'^create_issue/$', create_issue, name='create_issue'),
    url(r'^(?P<pk>\d+)/$', view_issue, name='view_issue'),
    url(r'^(?P<pk>\d+)/edit_issue/$', edit_issue, name='edit_issue'),
    url(r'^(?P<pk>\d+)/upvote/$', upvote_issue, name='upvote_issue'),
    url(r'^(?P<pk>\d+)/delete/$', delete_issue, name='delete_issue'),
    url(r'^(?P<pk>\d+)/comment/$', create_comment, name='create_comment'),
]