#!/usr/bin/python

# shellBlog: A simple command line blog
# Runs your favorite editor and appends the post to the index of a website
# stores the stories on the filesystem on a directory hierarchy based on the date
# Library File
# by default it will keep a local copy of your posts in the location specified on the
# LOCAL_PATH variable

# this little piece of code is licensed by the GPL v2
# (c) Ivan Chavero ichavero at chavero.com.mx




import os
import sys
import getopt
import datetime

"""

Preferences:

Change this variables to suit your needs

"""

#Directory in which the local posts are stored
LOCAL_PATH = "content"
#Drectory in which de remote posts are published
REMOTE_PATH = "web/content"
DEBUG = True
LOCAL = True


DEFAULT_POST = REMOTE_PATH + "/default.inc"
SCP = "scp -rp"


def check_dir(dir_name = LOCAL_PATH):
  """Checks if a directory exists, if it does not, it creates it
  """
  directory = os.path.dirname(dir_name)
  if not os.path.exists(directory):
    os.makedirs(directory)

def get_post_path(post_name = "post.inc"):
  """ Creates a path based on the current date and 
      the filename given on the command line
  """
  now = datetime.datetime.now()
  post_path = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
  full_path = LOCAL_PATH + "/" + post_path
  if not os.path.exists(full_path):
    os.makedirs(full_path)
  return(post_path)

def debug(msg):
  if DEBUG:
    print "DEBUG::" + msg
