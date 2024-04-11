from django.contrib import admin
from .models import LiftSystem
# Register your models here.
class LiftAdminSystem(admin.ModelAdmin):
    list_display = ('lift_name1', 'lift_name2','lift_no','floor_no','time_lift1','time_lift2')
    search_fields = ['lift_name']

admin.site.register(LiftSystem, LiftAdminSystem)