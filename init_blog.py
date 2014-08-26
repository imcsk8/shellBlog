#!/usr/bin/python

# shellBlog: A simple command line blog
# shellBlog is a set of scripts that perform the basic CRUD operations
# needed to manage posts on a server.
# it also provides a html template and javascript that allows you to
# navigate the posts on the web browser
#
# shellBlog is consists of 4 scripts: create.py, retrieve.py, update.py and delete.py

# init_blog.py:
# creates the web site skeleton for the blog:
# copies the desired template to the remote path

# this little piece of code is licensed by the GPL v2
# (c) Ivan Chavero ichavero at chavero.com.mx

import os
import sys
from blog.common import *
from blog.version import *
from optparse import OptionParser, OptionGroup, IndentedHelpFormatter

options = get_options()

# Sets command line options
DEBUG = options.debug
SERVER = options.server
LOCAL = options.keep_local

if options.remote_path:
    REMOTE_PATH = options.remote_path

print "Initializing the remote site on %s"
init_remote_site(SERVER, REMOTE_PATH)

