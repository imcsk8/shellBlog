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
from blog import common
from blog import version
from optparse import OptionParser, OptionGroup, IndentedHelpFormatter

#Directory in which the local posts are stored
LOCAL_PATH = "content"
#Drectory in which de remote posts are published
REMOTE_PATH = "web/content"
DEBUG = True
LOCAL = True

options = common.get_options()
   
# Sets command line options
DEBUG = options.debug
SERVER = options.server
LOCAL = options.keep_local

#get your default editor
editor = os.environ.get('EDITOR')
post_path = get_post_path()
#need to change this for a name, but it's late at night and i want to try this baby
file_path = LOCAL_PATH + "/" + post_path + "/post.inc"
command = editor + " " + file_path
debug("COMMAND: " + command)
os.system(command)

remote_file = post_path + "/post.inc"

#in the mean time we use the ssh commands
command = SCP + " " + LOCAL_PATH + "/* " + SERVER + ":" + REMOTE_PATH + "/."
debug("COMMAND: " + command)
os.system(command)

#create the default entry
set_default(SERVER, remote_file)

#in case you don't want to keep local copies of your posts
if not LOCAL:
  os.remove(LOCAL_PATH)
