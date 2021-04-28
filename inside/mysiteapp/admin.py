from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import prediction

# Register your models here.
admin.site.register(prediction)
