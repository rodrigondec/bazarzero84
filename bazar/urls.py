from django.conf.urls import url
from bazar import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^roupas/$', views.roupas, name='roupas'),
    url(r'^calcados/$', views.calcados, name='calcados'),
    url(r'^aderecos/$', views.aderecos, name='aderecos'),
    url(r'^add_pessoa/$', views.add_pessoa, name='add_pessoa'),
]
        