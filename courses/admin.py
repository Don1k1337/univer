from django.contrib import admin
from django.contrib.auth.models import Group
from . models import *

# Action func
def change_actuality(modeladmin, request, queryset):
    queryset.update(actuality = 'a')

# Action description
change_actuality.short_description = "Mark Selected Courses As Actual"

    

# Register your models here.
admin.site.register(Major)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'language', 'abbreviation', 'ccode', 'major')
    list_filter = ('title',)
    search_fields = ('title', 'abbreviation')
    ordering = ['title', 'abbreviation']
    actions = [change_actuality]

# Main Register for Models
admin.site.register(Course, CourseAdmin)

# Changing Admin header
admin.site.site_header = "IUCA Course System"
admin.site.unregister(Group)

