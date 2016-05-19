from rest_framework import viewsets, mixins
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from worker.models import Worker
from worker.serializers import WorkerSerializer

class WorkerViewSet(viewsets.GenericViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

    @list_route(methods=['post'])
    def setup(self, request):
        print('here')
        return Response({'result': 'Workers Started'})