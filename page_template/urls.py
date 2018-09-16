from django.conf.urls import include, url
from django.contrib import admin
from home.views import base
from django.views.static import serve
from django.views import static
'''not sure about one bellow'''
# from django.conf.urls.static import static
from .settings import MEDIA_ROOT
from accounts import urls as accounts_urls
from django.conf import settings

urlpatterns = [
    url(r'admin/', include(admin.site.urls)),
    url(r'^$', base, name='base'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'accounts/', include(accounts_urls)),

]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns



# '''can be problem with one bellow, in case so, delete!!!'''
# urlpatterns = [
#     # ... the rest of your URLconf goes here ...
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)