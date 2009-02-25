from django.conf.urls.defaults import *
from projects.models import Project

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.list_detail.object_list', {
        'queryset': Project.objects.all(),
        'template_object_name': 'project',
    }, 'project_list'),
    url(r'^update/(?P<slug>[-\w]+)/$', 'projects.views.update'),
    url(r'^(?P<slug>[-\w]+)/$', 'projects.views.project', name='project_detail'),
    url(r'^(?P<project>[-\w]+)/(?P<slug>[-_.\w]+)/$', 'projects.views.page', name='project_page_detail'),
)