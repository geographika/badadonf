#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = "Badadonf"
SITENAME = "Badadonf"
# SITEURL = "http://localhost:8000"

# Check if the environment variable exists
if "MY_SITE_URL" in os.environ:
    SITEURL = os.environ["MY_SITE_URL"]
else:
    # Set a default value if the environment variable is not found
    SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = "fr"
# LOCALE = ('usa') # "fr"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("FFBAD", "http://www.ffbad.org/"),
    ("Comité départemental de badminton du Val d'Oise", "http://www.cdbvo.fr/"),
)
# ,         ('Badadonf', 'http://badfab.free.fr/'))

# Social widget
# SOCIAL = (('You can add links in your config file', '#'), ('Another social link', '#'),)
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# My Settings

# THEME = "../pelican-bootstrap3"
THEME = "../pelican-bootstrap3-badadonf"
BOOTSTRAP_THEME = "united"

# https://github.com/wrobstory/pelican_dynamic

# https://github.com/mortada/pelican_javascript

PLUGIN_PATHS = ["../plugins"]  # "../pelican-plugins"]  # put the custom plugins first
# easiest to simply copy all plugins to the /plugins folder
PLUGINS = ["pdf-img", "i18n_subsites", "photos"]
JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n"],
}

I18N_TEMPLATES_LANG = "fr"

# do not process HTML files
READERS = {"html": None}

# SITELOGO = 'images/badadonf_fab.jpg'

PAGE_ORDER_BY = "page-order"

DISPLAY_PAGES_ON_MENU = True
# STATIC_PATHS = ['js','images']

STATIC_PATHS = [
    "images",
    "js",
    "pdfs",
    #'extra/robots.txt',
    "images/favicon.ico",
]
EXTRA_PATH_METADATA = {
    # 'extra/robots.txt': {'path': 'robots.txt'},
    "images/favicon.ico": {"path": "favicon.ico"}
}

# https://github.com/getpelican/pelican-plugins/tree/master/gallery
# see D:\GitHub\badadonf\pelican-plugins\photos\photos.py
# following assumes content build script is run from
# D:\GitHub\badadonf\website
PHOTO_LIBRARY = r"./content/images/gallery"
PHOTO_RESIZE_JOBS = -1  # debug or get errors
PHOTO_EXIF_KEEP = True
PHOTO_EXIF_AUTOROTATE = True  # true by default
