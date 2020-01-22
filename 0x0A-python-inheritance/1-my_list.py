#!/usr/bin/python3
'''
return list of all object attribute
'''


class MyList(list):
    '''def lookyp'''
    def print_sorted(self):
        s = []
        '''def sorted list'''
        s = self.copy()
        s.sort()
        print(s)
