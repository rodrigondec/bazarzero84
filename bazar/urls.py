from django.conf.urls import url
from bazar import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^roupas/$', views.roupas, name='roupas'),
    url(r'^calcados/$', views.calcados, name='calcados'),
    url(r'^aderecos/$', views.aderecos, name='aderecos'),
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^add_pessoa/$', views.add_pessoa, name='add_pessoa'),
]

# from django.conf.urls import patterns

# from smarturls import surl as url

# import views

# urlpatterns = patterns(
#     '',
#     url(regex=r'/events/<slug:slug>/jury/',
#         view=views.JuryView.as_view(),
#         name='jury_event'),
#     url(regex=r'/events/<slug:slug>/invite/jury/',
#         view=views.InviteEvent.as_view(),
#         name='event_invite_to_jury'),
#     url(regex=r'/events/<slug:slug>/remove/jury/<int:user_pk>/',
#         view=views.remove_user_from_event_jury,
#         name='event_remove_from_jury'),
# )
