from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.chat.urls')), 
    path('products/', include('core.products.urls')),
    path('manage-business/', include('core.manage_business.urls')),
    path('shops/', include('core.shops.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






