from django.conf.urls import url
from bazar import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
        