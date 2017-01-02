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


    # URLS DE admin
    url(r'^admin/$', views.interna, name='admin'),
    url(r'^admin/add_pessoa/$', views.add_pessoa, name='add_pessoa'),
    url(r'^admin/add_produto/$', views.add_produto, name='add_produto'),
    url(r'^admin/add_categoria_roupa/$', views.add_categoria_roupa, name='add_categoria_roupa'),
    url(r'^admin/add_roupa/$', views.add_roupa, name='add_roupa'),
    url(r'^admin/add_categoria_calcado/$', views.add_categoria_calcado, name='add_categoria_calcado'),
    url(r'^admin/add_calcado/$', views.add_calcado, name='add_calcado'),
    url(r'^admin/add_categoria_adereco/$', views.add_categoria_adereco, name='add_categoria_adereco'),
    url(r'^admin/add_adereco/$', views.add_adereco, name='add_adereco'),


    # URLS DE AUTENTICACAO
    url(r'^admin/login/$', auth_views.login, {'authentication_form': LoginForm}, name='login'),
    url(r'^admin/logout/$', auth_views.logout, name='logout'),

    url(r'^admin/password_change/$', auth_views.password_change, name='password_change'),
    url(r'^admin/password_change/done/$', auth_views.password_change_done, name='password_change_done'),

    url(r'^admin/password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^admin/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^admin/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^admin/reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]