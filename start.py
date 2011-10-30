#!/usr/bin/python

import os
import random
import re
import sys

DEFAULT_APP_NAME = 'baseapp'

def shell(commands):
    for c in commands.splitlines():
        if not c:
            continue
        print c
        os.system(c)

        
root_dir = os.getcwd()
root_dir_parts = root_dir.split('/')

if 'testrun' not in sys.argv:
    
    print 'App name: (baseapp): '
    app_name = raw_input()

else:
    print "TESTRUN"

print 'Renaming project folder to definitive name %(module_name)s'
shell('''git mv %s/static/content/%s %s/static/content/%s''' % \
      (DEFAULT_APP_NAME, DEFAULT_APP_NAME, app_name, app_name))
shell('''git mv %s/templates/content/%s %s/templates/content/%s''' % \
      (DEFAULT_APP_NAME, DEFAULT_APP_NAME, app_name, app_name))

shell('''git mv %s %s''' % (DEFAULT_APP_NAME, app_name))

if 'testrun' not in sys.argv:
    print 'Removing start.py and committing state...'
    shell('''git rm start.py
    git commit -m "Setup script"
    ''')

    