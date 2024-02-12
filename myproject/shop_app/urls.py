from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

urlpatterns = [
    path('orders/<int:customer_id>/', views.all_orders, name='all_orders'),
    path('client/<int:client_id>/', views.client_orders, name='client_orders'),
    path('newproduct/', views.newproduct, name='newproduct'),
    path('upload/', views.upload_image, name='upload_image'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
