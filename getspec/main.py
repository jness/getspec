#!/usr/bin/env python

import sys
import argparse
from re import compile
from urllib2 import urlopen, HTTPError

def get_link(package):
    '''get_link() retrieves the 'download file' link from the Launchpad files page'''
    url = 'http://bazaar.launchpad.net/~ius-coredev/ius/' + package + '/annotate/head%3A/SPECS/' + package +'.spec'
    request = urlopen(url)
    content = request.read()
    request.close()
    match = compile('<a href="(.*)">download file</a>').findall(content)
    match = 'http://bazaar.launchpad.net/' + match[0]
    return match

def get_download(link):
    '''get_download() returns the actual SPEC file from launchpad which can be printed'''
    request = urlopen(link)
    content = request.readlines()
    request.close()
    return content

def get_changelog(spec):
    '''get_changelog() uses the get_download() and parses for all content below %changelog'''
   
    linecount = 0
    changelog = False
    max_count = 0

    for line in spec:
        linecount += 1
        title = compile('%changelog').findall(line)
        
        # If we found %changelog using regex
        if title:
            changelog = linecount
        
        # If the changelog variable was set within title statement
        if changelog:
        
            # We only want to pull the last 5 changelog entries
            blank = compile('^$').findall(line)
            if blank:
                max_count += 1
                if max_count == 5:
                    sys.exit(0)
            
            print line,


def main():

    # Build my Parser with help for user input
    parser = argparse.ArgumentParser()
    parser.add_argument('package', help='IUS Package Name')
    parser.add_argument('--changelog', action='store_true', help='Print only the changelog')
    args = parser.parse_args()

    # Check URL has data, if not Package does not exisit
    try:
        url = get_link(args.package)
    except HTTPError as e:
        print e
        sys.exit(1)
 
    # Load the entire file to the spec variable
    spec = get_download(url)
 
    # If --changelog was passed the user only wants the changelog
    if args.changelog:
        get_changelog(spec)
    else:
    # If --changelog was NOT passed the user wants the entire SPEC
        for line in spec:
            print line,

if __name__ == '__main__':
    main()

