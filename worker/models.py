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

    topic1 = models.FloatField(default=0)
    topic2 = models.FloatField(default=0)
    topic3 = models.FloatField(default=0)
    topic4 = models.FloatField(default=0)
    topic5 = models.FloatField(default=0)
    topic6 = models.FloatField(default=0)
    topic7 = models.FloatField(default=0)
    topic8 = models.FloatField(default=0)
    topic9 = models.FloatField(default=0)
    topic10 = models.FloatField(default=0)
    topic11 = models.FloatField(default=0)
    topic12 = models.FloatField(default=0)
    topic13 = models.FloatField(default=0)
    topic14 = models.FloatField(default=0)
    topic15 = models.FloatField(default=0)
    topic16 = models.FloatField(default=0)
    topic17 = models.FloatField(default=0)
    topic18 = models.FloatField(default=0)
    topic19 = models.FloatField(default=0)
    topic20 = models.FloatField(default=0)
    topic21 = models.FloatField(default=0)
    topic22 = models.FloatField(default=0)
    topic23 = models.FloatField(default=0)
    topic24 = models.FloatField(default=0)
    topic25 = models.FloatField(default=0)

