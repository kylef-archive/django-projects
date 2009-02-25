from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.cache import cache_page
from django.http import Http404, HttpResponse
from projects.models import Project

#@cache_page
def page(request, project, slug):
    try:
        project = Project.objects.get(slug=project)
    except Project.DoesNotExist:
        raise Http404
    
    page = project.get_file(slug)
    if not page:
        raise Http404
    
    sidebar = project.get_file('sidebar')
    
    return render_to_response('projects/page_detail.html', {
        'project': project,
        'page': page,
        'side': sidebar,
        'page_title': slug.capitalize(),
    }, context_instance=RequestContext(request))
page = cache_page(page)

def project(request, slug):
    return page(request, slug, 'overview')

def update(request, slug):
    try:
        project = Project.objects.get(slug=slug)
    except Project.DoesNotExist:
        raise Http404
    
    project.update()
    return HttpResponse('done')