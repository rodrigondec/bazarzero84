from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^\Z', include('bazar.urls')),
    # url(r'^$', include('bazar.urls')),
    # url(r'^bazar/', include('bazar.urls')),
]