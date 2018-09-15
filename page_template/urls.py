from django.conf.urls import include, url
from django.contrib import admin
from home.views import base
from django.views import static
from accounts import urls as accounts_urls
from django.conf import settings

urlpatterns = [
    url(r'admin/', include(admin.site.urls)),
    url(r'^$', base, name='base'),
    url(r'accounts/', include(accounts_urls)),

]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns