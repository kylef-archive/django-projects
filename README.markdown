django-projects is a Django web application for displaying documentation of a git project.

### Downloading django-projects
You can download django-projects from the [git repository](http://github.com/kylef/django-projects/) or from the [zip file](http://github.com/kylef/django-projects/zipball/master).

### Installation
#### Using a package-management tool
One of the easiest way to install django-projects is by using a package-management tool, if you're not already familiar with the available package management tools Python. Now is a good time to get started.

One option is [easy_install](http://peak.telecommunity.com/DevCenter/EasyInstall), you can refer to its documentation to see how to get it set up. Once you've got it, you'll be able to type:

    easy_install django-projects

Another increasingly more popular option is [pip](http://pypi.python.org/pypi/pip/). Once again, refer to its documentation to get pip up and running, but once you have pip all setup and installed, you'll be able to type:

    pip install django-projects

#### Installing django-projects from git
If you have git installed on your computer, you can obtain the latest version of django-projects by typing::

    git clone git://github.com/kylef/django-projects.git

Inside the resulting "django-projects" directory will be a directory called "projects", which is the Python module for django-projects; you can symlink this from your Python path, or if you prefer use setup.py (more on that in Manually installing). You could also directly copy projects to your Python path, but this is not recommended. Symbolic links is one of the best ways for easy upgrading, at a later date, all you need to do is run ``git pull`` from inside django-projects folder.

#### Manually installing
To manually install django-projects, you will first need to download django-projects. You can find a link for this in the Downloading django-projects section above. Once you have a copy of django-projects, open it and run::

    python setup.py install

This will instal django-projects and will require administrative privileges on your computer as it is a system-wide install.

### How it works
Inside the admin panel of a Django project you will be able to add "Projects", a Project consists of a title, a description and a git project. When created, it will clone the git url to a local location. Once a project has been added, a user can visit ``/projects/<project>/`` to visit the main page of a project.

When a project page is opened, it will look for the associated page file in your git project. For example, when you visit ``/projects/django-projects/overview/`` you will see this file, docs/overview.txt because inside my project in the database. I have set the public folder is 'docs' and the extension is set to '.txt'. When a page is looked up, it will also look for the page ``sidebar``. Once the view has found all of this, it will pass the project, page, side (sidebar) and page_title to the template: ``projects/page_detail.html``.

When the url ``/projects/update/<project>/`` is visited, the git project will be updated. This can be useful when using github, a webhook could be set up so that your site always updates to any new commits.

### Where are projects stored locally?
Every project will be stored at: ``PROJECT_ROOT/<slug>``, so in your settings it is important to set ``PROJECT_ROOT = '/home/kylef/git/``.