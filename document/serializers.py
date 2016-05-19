from rest_framework import serializers
from document.models import Document, Tag, Neighbour
from worker.tasks import get_tags

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("position", "score", "tag", )

class NeighbourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighbour
        fields = ("url", "distance", )

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    neighbours = NeighbourSerializer(many=True, read_only=True)

    class Meta:
        model = Document
        fields = ("url", "document_title", "body", "tags", "neighbours", )
        read_only_fields = ("tagged", "url", )

    def create(self, validated_data):
        document = super(DocumentSerializer, self).create(validated_data)
        get_tags.delay(int(document.id))
        return document

