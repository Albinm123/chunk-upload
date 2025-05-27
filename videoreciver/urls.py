from django.urls import path
from .views import VideoChunkedUploadView, VideoChunkUploadCompleteView

urlpatterns = [
    path('upload/chunked/', VideoChunkedUploadView.as_view(), name='chunked-upload'),
    path('upload/chunked/<uuid:pk>/', VideoChunkedUploadView.as_view(), name='chunkedupload-detail'),
    path('upload/chunked/complete/', VideoChunkUploadCompleteView.as_view(), name='chunked-upload-complete'),
]