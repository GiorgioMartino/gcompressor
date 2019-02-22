#!/usr/bin/env python3

from distutils.core import setup
import os
import sys

setup(name='gcompress',
      version='1.0',
      description='LZW compressor and decompressor',
      author='Giorgio Martino',
      author_email='giorgio.martino.28@gmail.com',
      url='https://github.com/GiorgioMartino',
      packages=['gcompress'],
     )

os.system("sudo cp ~/Università/compressor/gcomp /bin")
os.system("sudo cp ~/Università/compressor/gdecomp /bin")

if (sys.argv[1] == 'install'):
    print('\n\nGCOMPRESS Package installed successfully.' +
        '\n\n\t- gcomp\t\tFile and directory compressor using LZW.' +
        '\n\t- gdecomp\tDecompressor for gcompself.' +
        '\n\nSee --help for more informations.' +
        '\nBUG Report: https://github.com/GiorgioMartino\n')
