from rest_framework import permissions
from drf_chunked_upload.views import ChunkedUploadView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import DroneVideo,MyChunkedUpload
from.serializers import DroneVideoChunkedUploadSerializer
from django.core.files import File

class VideoChunkedUploadView(ChunkedUploadView):
    """
    Handles uploading chunks of a video file.
    Inherits from drf_chunked_upload's ChunkedUploadView.
    """
    permission_classes = [permissions.IsAuthenticated]
    model = MyChunkedUpload
    field_name = "file"  
    serializer_class = DroneVideoChunkedUploadSerializer


class VideoChunkUploadCompleteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        upload_id = request.data.get("upload_id")
        if not upload_id:
            return Response({"error": "upload_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            chunked_upload = MyChunkedUpload.objects.get(id=upload_id)
        except MyChunkedUpload.DoesNotExist:
            return Response({"error": "Invalid upload_id"}, status=status.HTTP_404_NOT_FOUND)

        if not chunked_upload.completed:
            try:
                chunked_upload.assemble_chunks()
                chunked_upload.completed = True
                chunked_upload.save()
            except Exception as e:
                return Response({"error": f"Error assembling chunks: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            video = DroneVideo(file=File(chunked_upload.file, name=chunked_upload.filename),uploaded_by=request.user)
            video.save()
        except Exception as e:
            return Response({"error": f"Error saving video: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "video_id": video.id,
            "message": "Upload complete",
            "filename": video.file.name
        }, status=status.HTTP_201_CREATED)

