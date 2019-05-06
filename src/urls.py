from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('website/', include('Notepad.urls')),
    path('website/', include('ContactUs.urls')),
    path('website/auth/', include('authentication.urls')),
]


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)