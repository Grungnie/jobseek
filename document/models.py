from django.db import models

# Create your models here.
class Document(models.Model):
    app_label = 'document'

    document_title = models.CharField(max_length=256)
    body = models.TextField()


class Tag(models.Model):
    app_label = 'tag'

    position = models.IntegerField()
    score = models.FloatField()
    tag = models.CharField(max_length=256)

    document = models.ForeignKey('document.Document', related_name='tags')


class Neighbour(models.Model):
    app_label = 'neighbour'

    url = models.CharField(max_length=256)
    distance = models.FloatField()

    document = models.ForeignKey('document.Document', related_name='neighbours')