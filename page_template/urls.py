from django.conf.urls import include, url
from rest_framework import routers
from django.contrib import admin
from home.views import index, shop
from django.views.static import serve
from django.views import static
'''not sure about one bellow'''
from django.conf.urls.static import static
from .settings import MEDIA_ROOT
from accounts import urls as accounts_urls
from accounts import reset_urls as reset_urls
from blog import urls as blog_urls
from shop_cart import urls as shop_cart_urls
from shop_cart import views as shop_cart_views
from shop_categories import urls as shop_categories_urls
from shop_payments import urls as shop_payments_urls
from shop_products import urls as shop_products_urls
from shop_products import views as shop_product_views
from blog.views import post_list
from django.conf import settings
from search import urls as search_urls

router = routers.DefaultRouter()
router.register(r'products', shop_product_views.ProductViewSet)
router.register(r'users', shop_cart_views.UserViewSet)
router.register(r'cart', shop_cart_views.CartItemViewSet)


urlpatterns = [
    url(r'admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', index, name='index'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'accounts/', include(accounts_urls)),
    url(r'blog/', include(blog_urls)),
    url(r'^shop$', shop, name='shop'),
    url(r'^shop/cart/', include(shop_cart_urls)),
    url(r'^shop/categories/', include(shop_categories_urls)),
    url(r'^shop/payments/', include(shop_payments_urls)),
    url(r'^shop/products/', include(shop_products_urls)),
    url(r'^search/', include(search_urls)),

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