from rest_framework import serializers
from drf_chunked_upload.serializers import ChunkedUploadSerializer
from drf_chunked_upload.views import ChunkedUploadView
from .models import DroneVideo,MyChunkedUpload
from drf_chunked_upload.models import ChunkedUpload
import os

class DroneVideoChunkedUploadSerializer(ChunkedUploadSerializer):
    class Meta(ChunkedUploadSerializer.Meta):
        model = MyChunkedUpload
        fields = ChunkedUploadSerializer.Meta.fields
        
    def validate_file(self, file):
        # If file.name has no extension, likely a chunk upload: skip extension check
        ext = os.path.splitext(file.name)[1][1:].lower()  # extension without dot
        allowed_extensions = ['mp4', 'mov', 'avi', 'mkv']

        # Skip extension validation if filename has no extension (i.e., chunk upload)
        if not ext:
            return file  # allow chunk uploads without extension

        if ext not in allowed_extensions:
            raise serializers.ValidationError("Invalid file type.")

        if file.size > 1_000_000_000:
            raise serializers.ValidationError("File too large (max 1GB).")

        return file
    
    
class DroneVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneVideo
        fields = ['id', 'file', 'uploaded_by', 'uploaded_at']