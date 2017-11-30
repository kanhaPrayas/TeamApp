from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^v1/member(?:/(?P<id>[0-9]+))?/$', views.Member.as_view()),
]
