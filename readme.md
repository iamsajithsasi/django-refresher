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

### Customize modal table view in admin
```
+admin.py
    from django.contrib import admin
    from .models import SampleModel
    class SampleModalAdmin(admin.ModelAdmin):
        list_display = ('title', 'info')

        #change name of the columns and assign a value from object
        def info(self, obj):
            return obj.description

    # Register your models here.
    admin.site.register(SampleModel, SampleModalAdmin)
```

## Create RESTAPIs
