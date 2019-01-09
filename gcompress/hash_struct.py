#!/usr/bin/env python3
#-*- coding: utf-8 -*-

diz = {(-1,'a'):65, (-2,'a'):67}
diz
diz [-1,'b'] = 3

class hash:
    '''Implements data structure (hash map), search function and insert
    function'''
    def __init__(self):
        self.__h = {}

    def insert(self,p,x,c):
        '''Insert new node, after cheking it doesn't exists'''
        if (self.search(p,x) == -1):
            self.__h[p,x] = c

    def search(self,p,x):
        '''Search for a node father and label. If not found return -1'''
        try:
            return self.__h[p,x]
        except KeyError:
            return -1

    def print_hash(self):
        # for i in self.__h:
        print(self.__h)


# H = hash()
# H.insert(-1,'END',256)
# H.insert(-1,'a',65)
# H.insert(-1,'b',66)
#
# print(H.search(-1,'c'))
# H.print_hash()
