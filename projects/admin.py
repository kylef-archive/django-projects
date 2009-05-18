from django.contrib import admin
from projects.models import Project

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ('title', 'git')

admin.site.register(Project, ProjectAdmin)