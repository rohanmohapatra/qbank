from django.conf.urls import url, include

from knox.views import LogoutView

from .views import RegisterAPI, LoginAPI, UserAPI

urlpatterns = [
    url(r'^', include('knox.urls')),
    url(r'^register', RegisterAPI.as_view()),
    url(r'^login', LoginAPI.as_view()),
    url(r'^user', UserAPI.as_view()),
    url(r'^logout', LogoutView.as_view(), name='knox_logout')
]