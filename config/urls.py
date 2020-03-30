from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls import include, url
from django.views.static import serve
import os
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic.base import RedirectView
favicon_view = RedirectView.as_view(url=os.path.join(settings.STATIC_URL,'favicon.ico'), permanent=True)

urlpatterns = [
    path('favicon.ico', favicon_view),
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls')),
    path('auth/', obtain_auth_token),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
    url(r'^dmedia/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),

    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': os.path.join(settings.VUE_ROOT, 'media')}),
    url(r'^img/(?P<path>.*)$', serve,
        {'document_root': os.path.join(settings.VUE_ROOT, 'img')}),
    url(r'^js/(?P<path>.*)$', serve,
        {'document_root': os.path.join(settings.VUE_ROOT, 'js')}),
    url(r'^css/(?P<path>.*)$', serve,
        {'document_root': os.path.join(settings.VUE_ROOT, 'css')}),
    url(r'^fonts/(?P<path>.*)$', serve,
        {'document_root': os.path.join(settings.VUE_ROOT, 'fonts')}),
    url(r'^.*$', TemplateView.as_view(template_name="index.html")),
]
