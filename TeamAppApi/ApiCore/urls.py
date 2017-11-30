from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^v1/member(?:/(?P<id>[0-9]+))?/$', views.Member.as_view()),
    url(r'^v1/drf/member/$', views.CreateView.as_view(), name="create"),
    url(r'^v1/drf/member/(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name="details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
