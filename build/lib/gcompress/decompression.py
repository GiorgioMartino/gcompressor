#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gcompress import table_struct
import os
import stat


def file_decompress(f):
#Create file g without .Z extension, set same permissions
    g = ''+f[:-2]
    open(g,'a').close
    perm = stat.S_IMODE(os.lstat(f).st_mode)
    os.chmod(str(g),perm)

#Create and initialize the table with latin-1 code
    c = 256
    end = 256
    T = table_struct.table(c)
    T.insert(-1,'€')

#Open file f in read binary mode, g in write mode
    with open(f,'rb') as input, open(g,'w') as output:

#Read first char from file
        p = int.from_bytes(input.read(2), byteorder='big')

#Write first char on g
        alpha = T.text(p)
        output.write(alpha)
        x = alpha[0]

        while True:
#Read next seq with right size
            if (len(bin(c)) <= 18):
                q = int.from_bytes(input.read(2), byteorder='big')
            elif (len(bin(c)) <= 26):
                q = int.from_bytes(input.read(3), byteorder='big')
            else:
                q = int.from_bytes(input.read(4), byteorder='big')

            c += 1

#If q is not in the dict, add and write his value
            if (q >= c):
                T.insert(p,x)
                output.write(alpha+x)
#Else look up for the entire sequence
            else:
                alpha = T.text(q)
                x = alpha[0]
#If last char -> EOF
                if (x == '€'):
                    break;
                else:
                    T.insert(p,x)
                    output.write(alpha)
            p = q

#Close both files
    input.close()
    output.close()

    print("File {} decompressed successfully\n".format(f))
    os.remove(f)





def dir(d,r):
    recursive = r

#If -r not specified -> error
    if (not recursive):
        print("Cannot decompress directories. Type --help for [-r] option\n")
        return

#Recursive is true. For each object call the right function
    for i in os.listdir(d):
#If i is a compressed file
        if(os.path.isfile(os.path.join(d,i)) and i[-2:] == '.Z'):
            file_decompress(os.path.join(d,i))
#If i is a directory
        elif(os.path.isdir(os.path.join(d,i))):
            dir(os.path.join(d,i), recursive)
        else:
            print("Cannot decompress {} because it's not compressed\n".format(i))
