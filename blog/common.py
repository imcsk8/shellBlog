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
from blog import version
from optparse import OptionParser, OptionGroup, IndentedHelpFormatter


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

def set_main_story(server, remote_path, remote_file):
    #command = "ssh " + server + " 'cd " + REMOTE_PATH  + "; ln -sfn " + remote_file  + " default.inc' "
    command = "ssh %s 'cd %s; ln -sfn %s default.inc' " % (server, remote_path, remote_file)
    debug("COMMAND: " + command)
    os.system(command)

#def get_remote_post(server, remote_post_name = "post.inc"):
    #command = "scp %s:%s %s/." % (server, 
    #command = "scp " + server + " 'cd " + REMOTE_PATH  + "; ln -sfn " + remote_file  + " default.inc' "

def get_options():
    usage = "usage: %prog [options] [--help]"
    parser = OptionParser(usage=usage,version="%prog {0} {1}".format(version.release_string(), version.version_string()))
    parser.add_option("-s", "--server", help="The server in which to publish the posts")
    parser.add_option("-k", "--keep-local", default=True, help="Keep local files")
    parser.add_option("-d", "--debug", default=True, help="Keep local files")
    parser.add_option("-l", "--local-path", help="Set the local document path")
    parser.add_option("-r", "--remote-path", help="Set the remote document path")
    parser.add_option("-e", "--editor", default="vim", help="Set the editor")
    (options, args) = parser.parse_args()
    if not options.server:
        #printOptions()
        #opt_help = IndentedHelpFormatter()
        #opt_help.set_parser(parser)
        #opt_help.store_option_strings(parser)
        #    opt_help.option_strings = options
        #print opt_help.format_option(options.server)
        print "missing publishing server\n"
        raise SystemExit
    return options

def publish(local_path, server, remote_path):
    command = "%s %s/* %s:%s/." % (SCP, local_path, server, remote_path)
    debug("COMMAND: " + command)
    os.system(command)


def debug(msg):
  if DEBUG:
    print "DEBUG::" + msg
