from rest_framework import viewsets

from webapp.models import Photo
from webapp.serializers import PhotoSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = []

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PhotoSerializer
