from rest_framework import serializers
from document.models import Document


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document