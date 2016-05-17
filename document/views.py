from rest_framework import viewsets

from document.models import Document
from document.serializers import DocumentSerializer
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from sklearn.externals import joblib

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    @detail_route(methods=['get'])
    def tags(self, request, pk=None):
        document = self.get_object()

        # Load Model
        lda_model = joblib.load('worker/pickled_model/lda_model.pkl')

        # Get results
        result = lda_model.get_neighbours(document.body)

        return Response(result)