from django.conf.urls import url
from bazar import views
from django.contrib.auth import views as auth_views
from bazar.forms import LoginForm

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # URLS PUBLICAS
    url(r'^roupas/$', views.roupas, name='roupas'),
    url(r'^calcados/$', views.calcados, name='calcados'),
    url(r'^aderecos/$', views.aderecos, name='aderecos'),


    # URLS DE interna
    url(r'^interna/$', views.interna, name='interna'),
    url(r'^interna/add_pessoa/$', views.add_pessoa, name='add_pessoa'),


    # URLS DE AUTENTICACAO
    url(r'^interna/login/$', auth_views.login, {'authentication_form': LoginForm}, name='login'),
    url(r'^interna/logout/$', auth_views.logout, name='logout'),

    url(r'^interna/password_change/$', auth_views.password_change, name='password_change'),
    url(r'^interna/password_change/done/$', auth_views.password_change_done, name='password_change_done'),

    url(r'^interna/password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^interna/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^interna/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^interna/reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]