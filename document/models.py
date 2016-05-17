from django.db import models

# Create your models here.
class Document(models.Model):
    app_label = 'document'

    document_title = models.CharField(max_length=256)
    body = models.TextField()