import os
from django.db import models
from django.conf import settings

class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.CharField(max_length=384, blank=True, null=True)
    git = models.CharField(max_length=100, blank=True, null=True)
    public_folder = models.CharField(max_length=16, default='docs', help_text='Sub-folder of the project which has the public files. Example "docs"')
    extension = models.CharField(max_length=8, default='.txt', blank=True, null=True, help_text='An extension to any public viewable files inside the public folder')
    
    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        path = self.get_path()
        if not os.path.isdir(path):
            os.system('cd %s; git clone %s %s' % (settings.PROJECT_ROOT, self.git, self.slug))
        
        super(Project, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return ('project_detail', None, {'slug': self.slug})
    get_absolute_url = models.permalink(get_absolute_url)
    
    def get_path(self):
        return os.path.join(settings.PROJECT_ROOT, self.slug)
    
    def get_public_path(self):
        return os.path.join(self.get_path(), self.public_folder)
    
    def get_file(self, name):
        path = os.path.join(self.get_public_path(), '%s%s' % (name, self.extension))
        if os.path.isfile(path):
            return open(path, 'r').read()
        else:
            return ''
    
    def update(self):
        os.system('cd %s; git pull' % self.get_path())
