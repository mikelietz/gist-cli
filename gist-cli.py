#!/usr/bin/env python
import argparse
from ConfigParser import ConfigParser
import os.path
import urllib2
import json
import base64

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

  request = urllib2.Request( "%s/gists" % (uri) )

  raw = "%s:%s" % (username, password)
  auth = 'Basic %s' % base64.b64encode(raw).strip()
  request.add_header('authorization', auth)

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



