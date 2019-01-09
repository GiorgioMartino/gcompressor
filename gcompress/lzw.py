#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from hash import *

def compress(r,v,obj):
    # print("Recursive: {}\t\tVerbose: {}\nComprimo:".format(r,v))
    # for i in obj:
    #     print(i)

    obj_type []
    for i in obj:
        if(i[-2:] == '.Z'):                     #check last two characters
            print("{} cannot be compressed. Alredy done".format(i))
            return
        if(os.path.isfile(obj[i])):
            obj_type[i] = 0                    # 0 -> file     1 -> dir
        elif(os.path.isdir(obj[i])):
            obj_type[i] = 1
        else:
            print('Only files and dir can be compressed')
            return

    H = hash()
    H.insert(-1,'a')
    H.print_hash()



def decompress(r,obj):
    for i in obj:
        if(i[-2:] != '.Z'):
            print("{} cannot be uncompressed".format(i))
            return
    print("Recursive: {}\nComprimo:".format(r))
    for i in obj:
        print(i)
