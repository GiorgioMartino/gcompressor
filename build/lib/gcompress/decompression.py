#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gcompress import table_struct
import os
import stat


def file_decompress(f):
#Create file g without .Z extension, set same permissions
    g = ''+f[:-2]+'.D'
    open(g,'a').close
    perm = stat.S_IMODE(os.lstat(f).st_mode)
    os.chmod(str(g),perm)

#Create and initialize the table with ascii code
    c = 256
    T = table_struct.table(c)

#Open file f in read binary mode, g in write mode
    with open(f,'rb') as input, open(g,'w') as output:

#Read first 2 bytes from file
        p = int(input.read(2))
        print(p)
        # alpha = T.text(p)

    input.close()
    output.close()



def dir(d,r):
    pass
