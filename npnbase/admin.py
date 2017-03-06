from django.contrib import admin
from npnbase.models import *


class ZodiacsInline(admin.TabularInline):
    model = NameRecord.zodiacs.through
    extra = 2


class NameRecordAdmin(admin.ModelAdmin):
    fields = ['name', 'sex', 'description', 'groups']
    list_display = ('name', 'sex', 'description', 'groups')
    search_fields = ['name']
    inlines = [ZodiacsInline]


class GroupRecordAdmin(admin.ModelAdmin):
    fields = ['group_name']
    list_display = ('group_name',)
    search_fields = ['group_name']


admin.site.register(NameRecord, NameRecordAdmin)
admin.site.register(GroupRecord, GroupRecordAdmin)


admin.site.site_title = u'NomPreNom Admin'
admin.site.site_header = u'NomPreNom Admin'
