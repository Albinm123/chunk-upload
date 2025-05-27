# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from drf_chunked_upload.models import ChunkedUpload as BaseChunkedUpload

User = get_user_model()

def user_directory_path(instance, filename):
    return f'videos/user_{instance.uploaded_by.id}/{filename}'

class MyChunkedUpload(BaseChunkedUpload):
    class Meta:
        verbose_name = 'Chunked Upload'
        verbose_name_plural = 'Chunked Uploads'
        
class DroneVideo(models.Model):
    file = models.FileField(upload_to=user_directory_path)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Video {self.id} uploaded by {self.uploaded_by}"
    class Meta:
        abstract = False  