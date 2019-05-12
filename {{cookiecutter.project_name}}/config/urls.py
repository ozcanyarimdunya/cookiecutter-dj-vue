from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

admin.site.site_header = settings.SITE_HEADER
admin.site.site_title = settings.SITE_HEADER

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-token/', obtain_jwt_token),
    path('refresh-token/', refresh_jwt_token),

    # home page renderer
    path('', include('apps.common.urls'))
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
