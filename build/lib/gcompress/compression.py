#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gcompress import hash_struct
import os
import stat
import codecs


def file_compress(f,v):
#Create new file with .Z extension, set same permissions of the original
    verbose = v
    g = ''+f+'.Z'
    open(g,'a').close
    perm = stat.S_IMODE(os.lstat(f).st_mode)
    os.chmod(str(g),perm)

#Create and initialize the hash table with ascii characters
    c = 256
    end = 256
    H = hash_struct.hash(c)
    H.insert(-1,'END',end)
    # H.print_hash()

    p = -1

#Open file f in reading mode, file g in write binary mode
    with open(f) as input, open(g,'wb') as output:
        while True:
#Try to read one char, if not in the dictionary abort
            try:
                x = input.read(1)
            except:
                print('Encoding for char not supported.'.format(x))
                os.remove(g)
                return

            if not x:
                break;

            if(ord(x) > 255):
                print('Encoding for char -{}- not supported.'.format(x))
                os.remove(g)
                return

            q = H.search(p,x)

#If q is already in the dictionary, go deep and wait next char
            if (q != None):
                p = q
#Else write code on the file and add new sequence to dictionary
            else:
                if (len(bin(c)) <= 18):
                    output.write(p.to_bytes(2,'big'))
                else:
                    output.write(p.to_bytes(3,'big'))
                c += 1
                H.insert(p,x,c)
                p = H.search(-1,x)

#If p wasn't in the dictionary (special char) then add preventing crash
                if(p == None):
                    c += 1
                    H.insert(-1,x,c)
                    p = c

#Write last char, then close both files

        if (len(bin(c)) <= 18):
            output.write(p.to_bytes(2,'big'))
            output.write(end.to_bytes(2,'big'))
        else:
            output.write(p.to_bytes(3,'big'))
            output.write(end.to_bytes(3,'big'))

        input.close()
        output.close()
        # H.print_hash()

#Size input file and output file
    si, so = os.stat(f).st_size, os.stat(g).st_size

#If compressed is bigger remove, else print message
    if (si < so):
        os.remove(g)
        print("Compression on file {} does not reduce his size\n".format(f))
    elif (verbose):
        perc = (so/si)*100
        print("Compression achived for file {}: {:.2f}%\n".format(f,100-perc))
    else:
        print("File {} compressed successfully\n".format(f))





def dir(d,v,r):
    recursive = r
    verbose = v

#If -r not specified -> error
    if (not recursive):
        print("Cannot compress directories. Type --help for [-r] option\n")
        return

#Recursive option is true. For each item call respective function
    for i in os.listdir(d):
        # print(i)

#If is file and is not already compressed
        if(os.path.isfile(os.path.join(d,i)) and i[-2:] != '.Z'):
            file_compress(os.path.join(d,i),verbose)
#If is directory
        elif(os.path.isdir(os.path.join(d,i))):
            dir(os.path.join(d,i),verbose,recursive)
        else:
            print("{} is not suitable for compression. See --help\n".format(i))
