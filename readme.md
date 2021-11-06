# django-refresher

Django version 3.2.5

djangorestframework-3.12.4

os:ubuntu

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

## Register app in project

```
+settings.py

INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
    # go to myapp/apps.py file to get config name -> appname.apps.py.SnippetsConfigName
```

## Create API (Django Admin)

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

### Migrate or create table using the created model

```
python3 manage.py makemigrations
python3 manage.py migrate
```

## Customize admin

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

## Add ckeditor

```
+settings.py

INSTALLED_APPS = [
    ....
    'ckeditor',
]

optional:
CKEDITOR_CONFIGS = {
    'default': {
        # 'toolbar': 'Custom',
        'width': '461px',
        'height': 'auto',
        # 'toolbar_Custom': [
        #     ['Bold', 'Italic', 'Underline'],
        #     ['NumberedList', 'BulletedList'],
        # ],
    }
}

+models.py
from ckeditor.fields import RichTextField

class SampleModel(models.Model):
    details = RichTextField(blank=True, null=True)
```

## Change Heading

```
admin.site.site_header = 'My App'
```

## Create RESTAPIs (Create app -> api)

### Setup django-rest-framework

pip3 install djangorestframework

```
INSTALLED_APPS = [
    'rest_framework',
    ...
]
```

### Initial API (List)

1. Create a model

```
+models.py

from django.db import models
class ListModel(models.Model):

    title = models.CharField(null=False)
    description = models.TextField(null=True)


    class Meta:
        unique_together = ['title', 'description']
        
    def __str__(self):
        return self.title
```

2. Create Serializer

```
+ serializers.py

from rest_framework import serializers
from .models import ListModel

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListModel
        fields = "__all__"
```

3. Create a view

```
+views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ListSerializer
from .models import ListModel

@api_view(['GET'])
def ListView(request):
    list = ListModel.objects.all()
    serializer = ListSerializer(list, many=True)
    return Response(serializer.data)
```

3. Define URL

```
+urls.py

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('list/', views.ListView),
]
```

4. Register the app URLs in the project

```
+urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api.urls")),
    ...
]
```

5. Register in admin

```
+ admin.py

from .models import ListModel

# Register your models here.
admin.site.register(ListModel)
```

### Fetch a list by id

```
+views.py

@api_view(['GET'])
def DetailView(request, id):
    list = ListModel.objects.get(id=id)
    serializer = ListSerializer(list, many=False)
    return Response(serializer.data)

+urls.py

urlpatterns = [
    ...
    path('list/<str:id>/', views.DetailView),
]
```

### Create & Update

```
+views.py

@api_view(['POST'])
def CreateView(request):
    serializer = ListSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def UpdateView(request, id):
    list = ListModel.objects.get(id=id)
    serializer = ListSerializer(instance = list, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

+urls.py

urlpatterns = [
    ...
    path('create/', views.CreateView),
    path('update/<str:id>/', views.UpdateView),
]
```

### Delete

```
+views.py

@api_view(['DELETE'])
def DeleteView(request, id):
    list = ListModel.objects.get(id=id)
    list.delete()

    return Response("Item deleted success.")

+urls.py

urlpatterns = [
    ...
    path('delete/<str:id>/', views.DeleteView),
]
```

## Utils

Error: port is already in use

`killall -9 python3`
