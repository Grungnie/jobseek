from rest_framework import viewsets, mixins

from document.models import Document
from document.serializers import DocumentSerializer

class DocumentViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer