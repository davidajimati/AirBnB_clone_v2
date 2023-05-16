#!/usr/bin/env python3
'''
compresses all file in current directory into the 'versions' dir
creates the target folder is not exists
'''
from datetime import datetime
from fabric.api import local
import os.path


def do_pack():
    '''
    function to handle whole process
    '''
    # get current datetime in string format
    file = "versions/web_static_" + datetime.utcnow().strftime("%Y%m%d%H%M%S") + ".tgz"

    # connect and run command

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
