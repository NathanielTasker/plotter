from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^plotter/', include('plotter.urls')),
    url(r'^admin/', admin.site.urls),
]
