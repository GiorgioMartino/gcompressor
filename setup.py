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
      # license='MIT',
      packages=['gcompress'],
     )

os.system("sudo cp ~/Università/compressor/gcomp /bin")
os.system("sudo cp ~/Università/compressor/gdecomp /bin")

if (sys.argv[1] == 'install'):
    print('\n\n\nGCOMPRESS INSTALLED SUCCESSFULLY\n\n\n')
