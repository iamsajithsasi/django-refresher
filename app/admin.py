from django.contrib import admin
from .models import SampleModel

@admin.display(empty_value='NA')
class SampleModalAdmin(admin.ModelAdmin):
    list_display = ('title', 'info', 'year')
    # list_display_links = ('info',)
    list_filter = ('title', 'year')
    
    search_fields = ['title', 'description']
    
    # empty_value_display = 'NA'
    
    # fields = (('title', 'description', 'details'), 'year')
    
    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'description',)
    #     }),
    #     ('Other', {
    #         'classes': ('wide', 'extrapretty'),
    #         # 'classes': ('collapse'),
    #         'fields': ('year',),
    #     }),
    # )

    # formfield_overrides = { SampleModel.description: {'widget': RichTextEditorWidget},}

    # exclude = ('year',)

    
    def info(self, obj):
        return obj.description

# Register your models here.
admin.site.register(SampleModel, SampleModalAdmin)

