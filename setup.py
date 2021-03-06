# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from distutils.core import setup

setup(
    name='wagtailleaflet',
    packages=['wagtailleaflet', ],
    version='0.1',
    description='An application providing some template tags to add buttons to pages',
    author='François GUÉRIN',
    author_email='fguerin@ville-tourcoing.fr',
    url='https://github.com/frague59/django-buttons',
    download_url='https://github.com/frague59/django-buttons/tarball/0.1',
    keywords=['django', 'wagtail', 'leaflet'],
    classifiers=[],
    install_requires=['django-appconf',
              'wagtail>=1.9',
              'django-leaflet',
              'django-geojson', ]
)
