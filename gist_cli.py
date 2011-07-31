#!/usr/bin/env python
import argparse
from ConfigParser import ConfigParser
import os.path
import urllib2
import json
import sys
import base64

def main():
    parser = argparse.ArgumentParser( description = 'Create a github gist from a file, or from stdin' )
    parser.add_argument( 'infile_list', nargs = '*', type = argparse.FileType( 'r' ))
    parser.add_argument( '--description', '-d', default = '' )
    parser.add_argument( '--private', '-p', action = 'store_true', default = False )
    arguments = parser.parse_args()


    if len(arguments.infile_list) > 0:
        files = {}
        for infile in arguments.infile_list:
           files[infile.name] = {'content': infile.read()}
    else:
        files = {'stdin': {'content': sys.stdin.read()}}

    uri = 'https://api.github.com'

    request = urllib2.Request( '%s/gists' % (uri) )

    try:
        gitconfig = ConfigParser()
        gitconfig.readfp( open( os.path.expanduser( '~/.gitconfig' ) ) )
        username = gitconfig.get( 'github', 'user' )
        password = gitconfig.get( 'github', 'password' )
        raw = '%s:%s' % (username, password)
        auth = 'Basic %s' % base64.b64encode(raw).strip()
        request.add_header('authorization', auth)
    except: #Empty Excepts kill puppies
        pass

    request.add_data(json.dumps( {
        'description': arguments.description,
        'public': not arguments.private,
        'files': files,
    }))

    response = urllib2.urlopen(request)
    json_response = json.loads(response.read())
    print json_response['html_url']

if __name__ == '__main__':
  main()
