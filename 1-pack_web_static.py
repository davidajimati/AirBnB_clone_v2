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
    cur = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "web_static_" + cur

    # connect and run command
    local("mkdir -p versions")
    local("tar -czvf versions/{}.tgz *".format(file))

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {}".format(cur)).failed is True:
        return None
    return file
