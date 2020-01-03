#!/usr/bin/python3
<<<<<<< HEAD
# naaaaa paila

import tarfile
import os
from datetime import datetime


def do_pack():
    """ function do_pack """
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
=======
#asdfasdfa
>>>>>>> f01adaaadf3c63f1e63521dbdd6bb881109c4e0b
