#!/usr/bin/env python3
#-*- coding: utf-8 -*-


class hash:
    '''Implements data structure (hash map), search function and insert
    function'''

    def __init__(self,size):
        '''Initialize dictionary with ascii codes'''
        self.__h = {(-1,chr(i)):i for i in range(size)}

    def insert(self,p,x,c):
        '''Insert new node, after cheking it doesn't exists'''
        if (self.search(p,x) == None):
            self.__h[p,x] = c

    def search(self,p,x):
        '''Search for a node father and label. If not found return None'''
        try:
            return self.__h[p,x]
        except KeyError:
            return None

    def print_hash(self):
        # for i in self.__h:
        print(self.__h)
