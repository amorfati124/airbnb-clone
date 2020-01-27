from django.db import models

# Create your models here.


class TimesStampedModel(models.Model):
    """ timestamp  """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
