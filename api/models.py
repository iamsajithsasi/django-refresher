from django.db import models

# Create your models here.
class ListModel(models.Model):

    title = models.CharField(max_length=100, default='', null=False)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title