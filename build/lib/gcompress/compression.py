#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gcompress import hash_struct
import os
import stat
import math



def lg(x):
    if (x == 0):
        return 1
    else:
        return math.log(x)



def file_compress(f):
#Create new file with .Z extension, set same permissions of the original
    g = ''+f+'.Z'
    open(g,'a').close
    perm = stat.S_IMODE(os.lstat(f).st_mode)
    os.chmod(str(g),perm)

#Create and initialize the hash table with ascii characters
    end = 256
    size = end
    H = hash_struct.hash(end)
    # H.print_hash()

    p = -1

    with open(f) as input, open(g,'w') as output:
        while True:
            x = input.read(1)
#if EOF then exit
            if not x:
                break;
            q = H.search(p,x)
#If q is already in the dictionary, go deep and wait next char
            if (q != None):
                p = q
#Else write code on the file and add new sequence to dictionary
            else:
                output.write("{0:b}".format(p))
                size += 1
                H.insert(p,x,size)
                p = H.search(-1,x)
        output.write("{0:b}".format(p))
        # output.write(str(end))
        input.close()
        output.close()




def dir(d):
#Entro nella cartella e per ogni file chiamo file_compress()
    pass