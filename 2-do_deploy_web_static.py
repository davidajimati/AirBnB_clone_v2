#!/usr/bin/python3
'''
Fabric script to deploy an archive to
web servers using the function do_deploy
'''
from fabric.api import run, put, env
import os.path

env.hosts = ['3.84.238.139', '34.227.101.66']
env.user = 'ubuntu'


def do_deploy(archive_path):
    '''
    fabric function to handle the deployment
        takes file from local path and pushes it to
        remote web servers
    '''

    if os.path.exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        """ putting the file to .tgz """
        file_name = archive_path.split("/")[1]
        """ splitting .tgz """
        file_name2 = file_name.split(".")[0]
        """ spliting archivo """
        final_name = "/data/web_static/releases/" + file_name2 + "/"
        run("mkdir -p " + final_name)
        run("tar -xzf /tmp/" + file_name + " -C " + final_name)
        run("rm /tmp/" + file_name)
        run("mv " + final_name + "web_static/* " + final_name)
        run("rm -rf " + final_name + "web_static")
        run("rm -rf /data/web_static/current")
        run("ln -s " + final_name + " /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception:
        return False
