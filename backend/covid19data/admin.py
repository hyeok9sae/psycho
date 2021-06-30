from django.contrib import admin
from covid19data import models

# Register your models here.
admin.site.register(models.Covid19Info)
admin.site.register(models.Covid19GenAgeInfo)
admin.site.register(models.Covid19SidoInfo)
