from django.contrib import admin
from .models import Sample

@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ('sample_id', 'planet', 'sample_type', 'date_collected', 'collector')
    list_filter = ('sample_type', 'planet', 'date_collected')
    search_fields = ('sample_id', 'planet', 'description')
    date_hierarchy = 'date_collected'
    ordering = ('-date_collected',)
# Register your models here.
