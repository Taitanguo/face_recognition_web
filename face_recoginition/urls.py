# define face_recognition's url pattern
from django.conf.urls import url

from . import views

urlpatterns = [
    # main page
    url(r'^$', views.index, name = 'index')
]