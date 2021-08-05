from django.contrib import admin
from .models import SampleModel
class SampleModalAdmin(admin.ModelAdmin):
    list_display = ('title', 'info')
    def info(self, obj):
        return obj.description

# Register your models here.
admin.site.register(SampleModel, SampleModalAdmin)

