# -*- coding: utf-8 -*-

import os

#REPO_NAME = "myweb"  # Used for FREEZER_BASE_URL
DEBUG = True

# Assumes the app is located in the same directory
# where this file resides
APP_DIR = os.path.dirname(os.path.abspath(__file__))

def parent_dir(path):
    '''Return the parent of a directory.'''
    return os.path.abspath(os.path.join(path, os.pardir))

PROJECT_ROOT = parent_dir(APP_DIR)
# In order to deploy to Github pages, build the static files to 'docs'

FREEZER_DESTINATION =  os.path.join(PROJECT_ROOT, 'docs')

# Since this is a repo page (not a Github user page),
# we need to set the BASE_URL to the correct url as per GH Pages' standards
#FREEZER_BASE_URL = "http://localhost/".format(REPO_NAME)
# use relative URLS
FREEZER_RELATIVE_URLS = True
FREEZER_REMOVE_EXTRA_FILES = False  # IMPORTANT: If this is True, all app files
                                    # will be deleted when you run the freezer
