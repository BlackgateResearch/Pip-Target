#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import wsgiref.handlers

path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)

try:
    sys.path.remove(os.path.dirname(os.path.abspath(__file__)))
except ValueError:
    pass
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import gluon.main

wsgiref.handlers.CGIHandler().run(gluon.main.wsgibase)
