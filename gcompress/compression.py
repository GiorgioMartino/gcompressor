#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gcompress import hash_struct
import os
import stat
import struct


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

#Open file f in reading mode, file g in write binary mode
    with open(f) as input, open(g,'wb') as output:
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
                output.write(struct.pack('h',p))
                size += 1
                H.insert(p,x,size)
                p = H.search(-1,x)
#Write last char, then close both files
        output.write(struct.pack('h',p))
        # output.write(str(end))
        input.close()
        output.close()




def dir(d):
#Entro nella cartella e per ogni file chiamo file_compress()
#Devo però ricordarmi di controllare che siano tutti file prima.
#Una volta che inizio a comprimere devo poter arrivare fino alla fine
    pass
