from django.conf.urls import url, include
from .views import landing_page, create_issue

urlpatterns = [
    url(r'^$', landing_page, name='index'),
    url(r'^create_issue/$', create_issue, name='create_issue')
]