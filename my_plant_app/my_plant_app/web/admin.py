from django.contrib import admin

from my_plant_app.web.models import Plant, Profile


# Register your models here.

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass