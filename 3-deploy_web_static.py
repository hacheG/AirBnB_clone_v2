#!/usr/bin/python3
# i hate you holbi

from fabric.api import *
import os
from datetime import datetime
import tarfile

env.hosts = ["35.237.238.105", "34.74.131.167"]
env.user = "ubuntu"


def deploy():
    """ do_deploy"""
    tar = do_pack()
    if not tar:
        return False
    return do_deploy(tar)


def do_pack():
    """ bla bla bla and bla"""
    savedir = "versions/"
    filename = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
    if not os.path.exists(savedir):
        os.mkdir(savedir)
    with tarfile.open(savedir + filename, "w:gz") as tar:
        tar.add("web_static", arcname=os.path.basename("web_static"))
    if os.path.exists(savedir + filename):
        return savedir + filename
    else:
        return None


def do_deploy(archive_path):
    """ do_deploy_archive_path"""
    if not os.path.exists(archive_path):
        return False

    results = []

    res = put(archive_path, "/tmp")
    results.append(res.succeeded)

    basename = os.path.basename(archive_path)
    if basename[-4:] == ".tgz":
        name = basename[:-4]
    newdir = "/data/web_static/releases/" + name
    run("mkdir -p " + newdir)
    run("tar -xzf /tmp/" + basename + " -C " + newdir)

    run("rm /tmp/" + basename)
    run("mv " + newdir + "/web_static/* " + newdir)
    run("rm -rf " + newdir + "/web_static")
    run("rm -rf /data/web_static/current")
    run("ln -s " + newdir + " /data/web_static/current")

    return True
