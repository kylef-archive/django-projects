import cPickle as pickle
import datetime
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404, HttpResponse
from django.core import urlresolvers
from unipath import FSPath as Path
from projects.models import Project

def document(request, project, url):
    try:
        project = Project.objects.get(slug=project)
    except Project.DoesNotExist:
        raise Http404

    docroot = Path(project.get_pickle_path())

    # First look for <bits>/index.fpickle, then for <bits>.fpickle
    bits = url.strip('/').split('/') + ['index.fpickle']
    doc = docroot.child(*bits)
    if not doc.exists():
        bits = bits[:-2] + ['%s.fpickle' % bits[-2]]
        doc = docroot.child(*bits)
        if not doc.exists():
            raise Http404("'%s' does not exist" % doc)

    bits[-1] = bits[-1].replace('.fpickle', '')
    template_names = [
        'docs/%s.html' % '-'.join([b for b in bits if b]), 
        'docs/doc.html'
    ]
    
    return render_to_response(template_names, RequestContext(request, {
        'doc': pickle.load(open(doc, 'rb')),
        'env': pickle.load(open(docroot.child('globalcontext.pickle'), 'rb')),
        'update_date': datetime.datetime.fromtimestamp(docroot.child('last_build').mtime()),
        'home': project.get_absolute_url(),
        'redirect_from': request.GET.get('from', None),
    }))

def update(request, slug):
    try:
        project = Project.objects.get(slug=slug)
    except Project.DoesNotExist:
        raise Http404
    
    project.update()
    return HttpResponse('done')