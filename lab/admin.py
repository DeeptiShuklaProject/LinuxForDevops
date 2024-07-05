from django.contrib import admin
from lab.models import Lab

class LabAdmin(admin.ModelAdmin):
    list_display=('lab_title','lab_desc','lab_image','lab_slug')

admin.site.register(Lab,LabAdmin)

# Register your models here.
