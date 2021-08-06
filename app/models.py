from django.db import models

# Create your models here.
class SampleModel(models.Model):

    title = models.CharField(max_length=100, default='', null=False)
    description = models.TextField(null=True)
    year = models.DateField(blank=True, null=True)

    # for showing title in the admin tabs
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']