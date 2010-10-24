#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a WSGI handler for Apache
Requires apache+mod_wsgi.

In httpd.conf put something like:

    LoadModule wsgi_module modules/mod_wsgi.so
    WSGIScriptAlias / /path/to/wsgihandler.py

"""

# change these parameters as required
LOGGING = False
SOFTCRON = False

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)

try:
    sys.path.remove(os.path.dirname(os.path.abspath(__file__)))    
except ValueError:
    pass
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import gluon.main

if LOGGING:
    application = gluon.main.appfactory(wsgiapp=gluon.main.wsgibase,
                                        logfilename='httpserver.log',
                                        profilerfilename=None)
else:
    application = gluon.main.wsgibase

if SOFTCRON:
    from settings import settings
    settings.web2py_crontype = 'soft'
