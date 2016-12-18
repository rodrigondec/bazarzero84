from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^\Z', include('bazar.urls')),
    # url(r'^$', include('bazar.urls')),
    # url(r'^bazar/', include('bazar.urls')),
    url(r'^',  include('bazar.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
