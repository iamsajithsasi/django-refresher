# django-refresher

Django version 3.2.5

djangorestframework-3.12.4

## Ubuntu

1. sudo apt-get install python3-venv
2. mkdir djangoenv
3. python3 -m venv djangoenv
4. source djangoenv/bin/activate
5. pip install django
6. django-admin startproject projectname
7. cd projectname
8. python3 manage.py runserver

## Create admin

```
python3 manage.py migrate # apply all the default django changes
python3 manage.py createsuperuser
```

## Create App

`python3 manage.py startapp myapp`

## Create REST API

### Create model # myapp -> models.py

```
+ models.py
    class SampleModel(models.Model):
        title = models.CharField(max_length=100, default='', null=False)
        description = models.TextField(null=True)

        # for showing title in the admin tabs
        def __str__(self):
            return self.title

        # for ordering
        class Meta:
            ordering = ["-title"]

+ admin.py
    from .models import SampleModel

    # Register your model.
    admin.site.register(SampleModel)
```

### Create Django API Interface

pip3 install djangorestframework

```
INSTALLED_APPS = [
    'rest_framework',
    'myapp.apps.AppConfig',
    # go to myapp/apps.py file to get config name -> appname.apps.py.SnippetsConfigName
```

### Migrate or create table using the created model

```
python3 manage.py makemigrations
python3 manage.py migrate
```

### Customize admin

```
+admin.py
    from django.contrib import admin
    from .models import SampleModel

    @admin.display(empty_value='NA') # same as empty_value_display
    class SampleModalAdmin(admin.ModelAdmin):
        
        # <-- Table -start->

        # To display columns in table
        list_display = ('title', 'info', year)

        # To make a column item clickable link
        list_display_links = ('info',)
        
        # To add a search field
        search_fields = ['title', 'description']

        # To add filters
        list_filter = ('title', 'year')
        
        # To display the empty values
        empty_value_display = 'NA'

        # <-- Table -end->
        # <-- Form -start->

        # Group fields with an horizontal line
        fields = (('title', 'description'), 'year')

        # Group fields with an custom header (note: both fields and fieldsets cannot be at same time)
        fieldsets = (
            (None, {
                'fields': ('title', 'description',)
            }),
            ('Other', {
                'classes': ('collapse',), # wide -> without collapse button. +extrapretty
                'fields': ('year',),
            }),
        )

        # Exclude a field defined in model (excluded should not be added in fields)
        exclude = ('year',)


        # <-- Form -end->
        # <-- Other -->

        #Override any form field with text editor or any widget
        formfield_overrides = { SampleModel.description: {'widget': RichTextEditorWidget},}

        #change name of the columns and assign a value from object
        def info(self, obj):
            return obj.description

    # Register your models here.
    admin.site.register(SampleModel, SampleModalAdmin)
```

## Create RESTAPIs
