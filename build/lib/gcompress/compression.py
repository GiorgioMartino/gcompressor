#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gcompress import hash_struct
import os
import stat

from inspect import currentframe, getframeinfo


# def lg(x):
#     from math import log2
#     if (x == 0):
#         return 1
#     else:
#         return int(log2(x))+1


def file_compress(f,v):
#Create new file with .Z extension, set same permissions of the original
    verbose = v
    g = ''+f+'.Z'
    open(g,'a').close
    perm = stat.S_IMODE(os.lstat(f).st_mode)
    os.chmod(str(g),perm)

#Create and initialize the hash table with ascii characters
    c = 256
    H = hash_struct.hash(c)
    # H.print_hash()

    p = -1

#Open file f in reading mode, file g in write binary mode
    with open(f) as input, open(g,'wb') as output:
        while True:
            try:
                x = input.read(1)
            except:
                print("File format not supported for compression.")
                return
#if EOF then exit
            if not x:
                break;
            q = H.search(p,x)
#If q is already in the dictionary, go deep and wait next char
            if (q != None):
                # print("Before p = q -> {}".format(p))
                p = q
                # print("After p = q -> {}".format(p))
                # print('q = {}, p = {}'.format(q,p))
#Else write code on the file and add new sequence to dictionary
            else:

#HANDLE THE ERROR WHERE P BECOMES NONE
                if(p == None):
                    print("Error")
                    print("{} value of c".format(c))
                    print("{} is last char".format(x))


                if (len(bin(p)) <= 18):
                    output.write(p.to_bytes(2,'big'))
                else:
                    output.write(p.to_bytes(3,'big'))
                # print('q = {}, p = {}'.format(q,p))
                c += 1
                H.insert(p,x,c)
                # print("Before p = H.search -> {}".format(p))
                p = H.search(-1,x)
                if(p == None):
                    c+=1
                    H.insert(-1,x,c)
                    p = c
                # print("After p = H.search -> {}\nX = {}".format(p,x))
#Write last char, then close both files
        if (len(bin(p)) <= 18):
            output.write(p.to_bytes(2,'big'))
        else:
            output.write(p.to_bytes(3,'big'))

        input.close()
        output.close()
        # H.print_hash()


#If verbose mode was specified print % of compression
    si, so = os.stat(f).st_size, os.stat(g).st_size

    if (si < so):
        os.remove(g)
        print("Compression on file {} does not reduce his size\n".format(f))
    elif (verbose):
        perc = (so/si)*100
        print("Compression achived for file {}: {:.2f}%\n".format(f,100-perc))
    else:
        print("File {} compressed successfully\n".format(f))
#Check if compressed file is smaller. If not don't compress





def dir(d,v,r):
#Entro nella cartella e per ogni file chiamo file_compress()
#Devo però ricordarmi di controllare che siano tutti file prima.
#Una volta che inizio a comprimere devo poter arrivare fino alla fine

#-r = se uno degli argomenti è una dir scendo e comprimo tutti i file
#che trovo
    recursive = r
    verbose = v
    if (not recursive):
        print("Cannot compress directories. Type --help for [-r] option\n")
        return
#Recursive option is true. For each item call respective function
    for i in os.listdir(d):
        print(i)
        if(os.path.isfile(os.path.join(d,i)) and i[-2:] != '.Z'):
            file_compress(os.path.join(d,i),verbose)
        elif(os.path.isdir(os.path.join(d,i))):
            dir(os.path.join(d,i),verbose,recursive)
        else:
            print("{} is not suitable for compression. See --help\n".format(i))
