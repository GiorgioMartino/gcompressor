#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gcompress import table_struct
import os
import stat


def file_decompress(f):
#Create file g without .Z extension, set same permissions
    g = ''+f[:-2]+'.D'
    open(g,'a').close
    perm = stat.S_IMODE(os.lstat(f).st_mode)
    os.chmod(str(g),perm)

#Create and initialize the table with ascii code
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
            if (len(bin(c)) <= 18):
                q = int.from_bytes(input.read(2), byteorder='big')
            else:
                q = int.from_bytes(input.read(3), byteorder='big')

            c += 1

            if (q >= c):
                T.insert(p,x)
                output.write(alpha+x)
            else:
                alpha = T.text(q)
                x = alpha[0]
                if (x == '€'):
                    break;
                else:
                    T.insert(p,x)
                    output.write(alpha)
            p = q
    input.close()
    output.close()





def dir(d,r):
    pass
