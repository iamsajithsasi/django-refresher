from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
class SampleModel(models.Model):

    title = models.CharField(max_length=100, default='', null=False)
    description = models.TextField(null=True)
    details = RichTextField(blank=True, null=True)
    year = models.DateField(blank=True, null=True)

    # for showing title in the admin tabs
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']