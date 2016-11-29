from django.contrib import admin
from npnbase.models import *


class ZodiacsInline(admin.TabularInline):
    model = NameRecord.zodiacs.through
    extra = 3


class NameRecordAdmin(admin.ModelAdmin):
    fields = ['name', 'sex', 'description', 'groups']
    list_display = ('name', 'sex', 'description', 'groups')
    search_fields = ['name']
    inlines = [ZodiacsInline]


admin.site.register(NameRecord, NameRecordAdmin)
