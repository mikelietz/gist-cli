#!/usr/bin/env python
import argparse
from ConfigParser import ConfigParser
import os.path
import urllib2
import json

def main():
  parser = argparse.ArgumentParser( description = 'Create a github gist from a file.' )
  parser.add_argument( 'infile_list', nargs = '+', type = argparse.FileType( 'r' ) )
  parser.add_argument( '--description', '-d', default = '' )
  parser.add_argument( '--private', '-p', action = 'store_true', default = False ) # not used yet.
  arguments = parser.parse_args()

  for infile in arguments.infile_list:
     file_name = infile.name
     file_data = infile.read()

  uri = "https://api.github.com"
  gitconfig = ConfigParser()
  gitconfig.readfp( open( os.path.expanduser( "~/.gitconfig" ) ) )
  username = gitconfig.get( "github", "user" )
  password = gitconfig.get( "github", "password" )

  # Build an HTTP Client with the HTTPBasic Authentication built in
  password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
  password_mgr.add_password( None, uri, username, password )
  handler = urllib2.HTTPBasicAuthHandler( password_mgr )
  opener = urllib2.build_opener( handler )
  urllib2.install_opener( opener )

  request = urllib2.Request( "%s/gists" % (uri) )
  request.add_data( json.dumps( {
      "description": arguments.description,
      "public": arguments.private,
      "files": {
          file_name: {
              "content": file_data,
          },
      },
  }))

  response = urllib2.urlopen( request )
  json_response = json.loads(response.read())
  print json_response['html_url']

#  print response #[ 'html_url' ]
 
if __name__ == '__main__':
  main()



