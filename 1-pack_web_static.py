#!/usr/bin/env python3
from datetime import datetime
from fabric import Connection

def do_pack():
    # get current datetime in string format
    cur = datetime.now().strftime("%Y%m%d%H%M%S")
    cur = "web_static_" + cur
    # connect to localhost
    conn = Connection('localhost')

    # connect and run command
    conn.local("mkdir -p versions")
    conn.local("tar -czvf versions/{}.tgz *".format(cur))
