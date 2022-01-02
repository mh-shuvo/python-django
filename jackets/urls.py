from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from product import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/latest-product/', views.LatestProductList.as_view()),
    path('api/v1/products/<slug:category_slug>/<slug:product_slug>',
         views.ProductDetail.as_view()),
    path('api/v1/products/<slug:category_slug>/',
         views.CategoryDetails.as_view()),
    path('api/v1/products/search',
         views.search),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
