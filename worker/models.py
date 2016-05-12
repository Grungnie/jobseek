from django.db import models

# Create your models here.
class JobDescription(models.Model):
    app_label = 'job_description'

    url = models.CharField(max_length=256)

    heading = models.CharField(max_length=256)

    work_type = models.CharField(max_length=256)
    classification = models.CharField(max_length=256)
    sub_classification = models.CharField(max_length=256)

    address_locality = models.CharField(max_length=265)
    address_region = models.CharField(max_length=265)

    body = models.TextField()