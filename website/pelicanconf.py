#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Badadonf'
SITENAME = u'Badadonf'
#SITEURL = 'http://badadonf.tk'
#SITEURL = "http://localhost:8000"
SITEURL = ''
PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('FFBAD', 'http://www.ffbad.org/'),
    ("Comité départemental de badminton du Val d'Oise", 'http://www.cdbvo.fr/'),)
# ,         ('Badadonf', 'http://badfab.free.fr/'))

# Social widget
#SOCIAL = (('You can add links in your config file', '#'), ('Another social link', '#'),)
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# My Settings

THEME = '../../pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'united'

#https://github.com/wrobstory/pelican_dynamic

# https://github.com/mortada/pelican_javascript

PLUGIN_PATHS = ['../../pelican-plugins']
PLUGINS = ['pelican_javascript']

# do not process HTML files
READERS = {'html': None}

#SITELOGO = 'images/badadonf_fab.jpg'

DISPLAY_PAGES_ON_MENU = True
STATIC_PATHS = ['js','images']

STATIC_PATHS = [
    'images', 
    'js',
    #'extra/robots.txt', 
    'extra/favicon.png'
]
EXTRA_PATH_METADATA = {
   # 'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.png'}
}