#!/usr/bin/python

# shellBlog: A simple command line blog
# shellBlog is a set of scripts that perform the basic CRUD operations
# needed to manage posts on a server.
# it also provides a html template and javascript that allows you to
# navigate the posts on the web browser
#
# shellBlog is consists of 4 scripts: create.py, retrieve.py, update.py and delete.py

# create.py:
# Runs your favorite editor and appends the post to the index of a website
# stores the stories on the filesystem on a directory hierarchy based on the date
# simple, and easy just:
# ./create.py myhost.com
# it will run your favorite editor and copy (publish) the story to the server.
# you need a index.html file smart enough to load the published files
# this is a work in progress, you can fix it if you like it, just send me the changes :)
# by default it will keep a local copy of your posts in the location specified on the
# LOCAL_PATH variable on blog.py

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

if options.local_path:
    LOCAL_PATH = options.local_path

if options.remote_path:
    REMOTE_PATH = options.remote_path

#environment variable takes precedence
if os.environ.get('EDITOR'):
    editor = os.environ.get('EDITOR')
else:
    editor = options.editor

post_path = get_post_path()
#need to change this for a name, but it's late at night and i want to try this baby
file_path = LOCAL_PATH + "/" + post_path + "/post.inc"
command = editor + " " + file_path
debug("COMMAND: " + command)
os.system(command)

remote_file = post_path + "/post.inc"

#in the mean time we use the ssh commands
#command = SCP + " " + LOCAL_PATH + "/* " + SERVER + ":" + REMOTE_PATH + "/."
publish(LOCAL_PATH, SERVER, REMOTE_PATH)

#create the default entry
set_main_story(SERVER, REMOTE_PATH, remote_file)

#in case you don't want to keep local copies of your posts
if not LOCAL:
  os.remove(LOCAL_PATH)
