#!/usr/bin/python

# shellBlog: A simple command line blog
# shellBlog is a set of scripts that perform the basic CRUD operations
# needed to manage posts on a server.
# it also provides a html template and javascript that allows you to
# navigate the posts on the web browser
#
# shellBlog is consists of 4 scripts: create.py, retrieve.py, update.py and delete.py

# update.py:
# Runs your favorite editor and appends the post to the index of a website
# stores the stories on the filesystem on a directory hierarchy based on the date
# simple, and easy just:
# ./update.py myhost.com
# it will also set the default post if we give it a second argument with the 
# appropiate path


# this little piece of code is licensed by the GPL v2
# (c) Ivan Chavero ichavero at chavero.com.mx

import os
import sys
from blog import *

SERVER = ""
DEFAULT_POST = ""

if len(sys.argv) <= 2:
  print "Usage: " + sys.argv[0] + " <server filename> <post path>"
  exit()

SERVER = sys.argv[1]


#get your default editor
editor = os.environ.get('EDITOR')
#need to change this for a name, but it's late at night and i want to try this baby
file_path = LOCAL_PATH + "/" + sys.argv[2]
command = editor + " " + file_path
debug("COMMAND: " + command)
os.system(command)

#in the mean time we use the ssh commands
command = SCP + " " + LOCAL_PATH + "/* " + SERVER + ":" + REMOTE_PATH + "/."
debug("COMMAND: " + command)
os.system(command)
#create the default entry
#remote_file = REMOTE_PATH + "/" + post_path + "/post.inc"
remote_file = sys.argv[2]
set_default(SERVER, remote_file)

#in case you don't want to keep local copies of your posts
if not LOCAL:
  os.remove(LOCAL_PATH)
