from rest_framework import viewsets, mixins
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from time import sleep

from worker.models import Worker
from worker.serializers import WorkerSerializer
from worker.tasks import build_model

from jobseek.celery import app



class WorkerViewSet(viewsets.GenericViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

    @list_route(methods=['post'])
    def setup(self, request):
        # Allocate the worker to build model
        app.control.add_consumer('build_model', destination=['worker0@Nerd-Box'], reply=False)

        # Grow the pool to 4
        print(app.control.pool_grow(destination=['worker0@Nerd-Box',], reply=False, n=3))
        sleep(1)

        return Response({'result': 'Allocated Build Workers'})

    @list_route(methods=['post'])
    def build_model(self, request):
        build_model.apply_async([], queue='build_model', time_limit=3600)
        return Response({'result': 'Started Build'})