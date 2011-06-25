#!/usr/bin/env python
from distutils.core import setup
import projects

setup(
    name='django-projects',
    version='%s' % projects.__version__,
    description='django-projects is a Django web application for displaying documentation of a git project.',
    author='Kyle Fuller',
    author_email='inbox@kylefuller.co.uk',
    url='http://kylefuller.co.uk/projects/django-projects/',
    download_url='http://cloud.github.com/downloads/kylef/django-projects/django-projects-%s.zip' % projects.__version__,
    packages=['projects'],
    package_data={'projects': ['templates/base.html', 'templates/projects/*.html']},
    requires='unipath',
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ]
)
