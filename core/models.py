from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # extra information
    class Meta:
        # abstract model 은 DB에 나타나지 않습니다.
        abstract = True
