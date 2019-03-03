#!/usr/bin/env python2
# Create Windows VMs in Vagrant Virtualbox
# Bas Meijer 2019

import requests
import urllib
import os
import zipfile

text_file = open("boxes.txt", "r")
box_urls = text_file.readlines()

text_file = open("archives.txt", "r")
zipfiles = text_file.readlines()

for box_url in box_urls:
    i = 0
    download = 'curl -o ' + zipfiles[i].rstrip() + ' ' + box_url
    try:
        print download
        os.system(download)
        i += 1
    except Exception as e:
        print(e)
        i += 1
        continue

for boxzip in zipfiles:
    print boxzip.rstrip()
    zip = zipfile.ZipFile(boxzip.rstrip(), 'r')
    nameparts = boxzip.split(".")
    boxname = nameparts[0] + '.' + nameparts[1]
    print boxname

    try:
        box = zip.namelist()[0]
        print box
        zip.extractall()
        vagrant_call = 'vagrant box add -f --provider virtualbox --name ' + \
            boxname + " '" + box + "'"
        print vagrant_call
        os.system(vagrant_call)
    except IOError as e:
        print e
        continue
