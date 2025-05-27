from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
import os
# from drf_chunked_upload import urls as chunked_upload_urls
# from drf_chunked_upload.views import ChunkedUploadViewSet

# router = DefaultRouter()
# router.register(r'upload/chunked', ChunkedUploadViewSet, basename='chunkedupload')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('videoreciver.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # get token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    # path('api/', include(router.urls)),# refresh token
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
if settings.DEBUG or os.environ.get('RENDER'):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)