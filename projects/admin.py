from django.contrib import admin
from projects.models import Project

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ('title', 'git')
    fieldsets = (
        (None, {'fields': ('title', 'description', 'git')}),
        ('Extra', {'fields': ('public_folder', 'extension', 'slug')})
    )

admin.site.register(Project, ProjectAdmin)