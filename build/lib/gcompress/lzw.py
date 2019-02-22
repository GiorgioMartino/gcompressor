#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from gcompress import compression, decompression


def compress(r,v,obj):
#Check if all args aren't compressed yet, and if they are only
#files or dir. Then call respective function
    for i in obj:
        if(i[-2:] == '.Z'):
            print('{} cannot be compressed. Alredy done'.format(i))
            break
        if(not os.path.isfile(i)) and (not os.path.isdir(i)):
            print('Only files and dir can be compressed.')
            break
        elif(os.path.isfile(i)):
            if(os.stat(i).st_size > 0):
                compression.file_compress(i,v)
            else:
                print('File with size 0 cannot be compressed.')
        else:
            compression.dir(i,v,r)




def decompress(r,obj):
#Check what can be passed to decompression, else print message
    for i in obj:
        if(os.path.isfile(i) and i[-2:] == '.Z'):
            decompression.file_decompress(i)
        elif(os.path.isdir(i)):
            decompression.dir(i,r)
        else:
            print("Cannot decompress {}. See --help.".format(i))
