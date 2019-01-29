#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class table:
    '''Data structure for decompression. Implements insert and
    text function'''

    def __init__(self,size):
        '''Initialize list with ascii codes'''
        self.__t = []
        for i in range(size):
            self.__t.append((-1,chr(i)))


    def insert(self,p,x):
        '''Append new node to the list'''
        self.__t.append((p,x))


    def text(self,p):
        '''Return full text sequence'''
        s = []
#Get reverse string
        while (p != -1):
            s.append(self.__t[p][1])
            p = self.__t[p][0]
#Return in the right order
        s.reverse()
        alpha = ""
        for i in s:
            alpha += i
        return alpha


    def print_table(self):
        for i in range(len(self.__t)):
            print(self.__t[i])
