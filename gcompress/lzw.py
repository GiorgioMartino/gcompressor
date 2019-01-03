#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def compress(r,v,obj):
    # print("Recursive: {}\t\tVerbose: {}\nComprimo:".format(r,v))
    # for i in obj:
    #     print(i)
    type []
    for i in obj:
        if(i[-2:] == '.Z'):
            print("{} cannot be compressed. Alredy done".format(i))
            return
        if(os.path.isfile(obj[i])):
            t = 0                    # 0 -> file     1 -> dir
        elif(os.path.isdir(obj[i])):
            t = 1
        else:
            print('Only files and dir can be compressed')
            return




def decompress(r,obj):
    for i in obj:
        if(i[-2:] != '.Z'):
            print("{} cannot be uncompressed".format(i))
            return
    print("Recursive: {}\nComprimo:".format(r))
    for i in obj:
        print(i)
