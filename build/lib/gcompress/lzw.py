#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def compress(r,v,obj):
    print("Recursive: {}\t\tVerbose: {}\nComprimo:".format(r,v))
    for i in obj:
        print(i)

def decompress(r,obj):
    for i in obj:
        if(i[-2:] != '.Z'):
            print("{} cannot be uncompressed".format(i))
            return
    print("Recursive: {}\nComprimo:".format(r))
    for i in obj:
        print(i)
