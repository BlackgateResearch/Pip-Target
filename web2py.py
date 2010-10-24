#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(path)
except NameError:
    path = os.getcwd() # Seems necessary for py2exe
    
try:
    sys.path.remove(os.path.dirname(os.path.abspath(__file__)))
except ValueError:
    pass
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# import gluon.import_all ##### This should be uncommented for py2exe.py
import gluon.widget

# Start Web2py and Web2py cron service!
gluon.widget.start(cron=True)
