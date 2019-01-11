#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from gcompress import compression

def compress(r,v,obj):
    # print("Recursive: {}\t\tVerbose: {}\nComprimo:".format(r,v))
    # for i in obj:
    #     print(i)

#Check if all args aren't compressed yet, and if they are only files or dir
    for i in obj:
        if(i[-2:] == '.Z'):                     #check last two characters
            print('{} cannot be compressed. Alredy done'.format(i))
            return
        if(not os.path.isfile(i)) and (not os.path.isdir(i)):
            print('Only files and dir can be compressed')
            return

    for i in obj:
        if(os.path.isfile(i)):
            compression.file_compress(i)
        else:
            compression.dir(i)





def decompress(r,obj):
    for i in obj:
        if(i[-2:] != '.Z'):
            print("{} cannot be uncompressed".format(i))
            return
    print("Recursive: {}\nComprimo:".format(r))
    for i in obj:
        print(i)
