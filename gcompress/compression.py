#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gcompress import hash_struct
import os
import shutil
import stat

def file_compress(f):
#Create a copy of file given, set same permissions
    g=""+f+".Z"
    shutil.copyfile(f,g)
    perm = stat.S_IMODE(os.lstat(f).st_mode)
    os.chmod(g,perm)


def dir(d):
#Entro nella cartella e per ogni file chiamo file_compress()
    pass
