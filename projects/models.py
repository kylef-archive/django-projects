import os
from django.db import models
from django.conf import settings

class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.CharField(max_length=384, blank=True, null=True)
    git = models.CharField(max_length=100, blank=True, null=True, help_text='URI of the git repository.')
    docs = models.CharField(max_length=16, default='docs', help_text='Sub-folder of the project which has the documentation. Example "docs"')
    
    class Meta:
        ordering = ('title',)
    
    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super(Project, self).save(*args, **kwargs)
        path = self.get_path()
        if not os.path.isdir(path):
            os.system('cd %s; git clone %s %s' % (settings.PROJECT_ROOT, self.git, self.slug))
        
        self.update()
    
    def get_absolute_url(self):
        return ('project_detail', None, {'project': self.slug})
    get_absolute_url = models.permalink(get_absolute_url)
    
    def get_path(self):
        return os.path.join(settings.PROJECT_ROOT, self.slug)
    
    def get_docs_path(self):
        return os.path.join(self.get_path(), self.docs)
    
    def get_pickle_path(self):
        return os.path.join(self.get_docs_path(), '_build/pickle')
    
    def update(self):
        os.system('cd %s; git pull' % self.get_path())
        os.system('cd %s; make pickle' % self.get_docs_path())
