#! /usr/bin/env python

class HashTable():
    def __init__(self,length):
        self.table = []
        self.length = length
        for i in xrange(self.length):
            self.table.append([])

    def modhash(self,string):
        """string input is len(9)"""
        sum = 0
        for i in string:
            sum+=ord(i)
        return (sum % self.length)


    #TODO add basic operation

    def add(self,string):
        tmphash = self.modhash(string)
        self.table[tmphash].append(string)

    def search(self,string):
        tmphash = self.modhash(string)
        for element in self.table[tmphash]:
            if (string == element):
                return True
        #Didn't find it
        return False

    def pprint(self):
        for row in self.table:
            length = len(row)
            if(length > 8):
                #short print
                import sys
                for i in range(7):
                    sys.stdout.write("["+str(row[i])+"] ")

                sys.stdout.write("[...] ")
                sys.stdout.write("["+str(row[-1])+"]\n")
            else:
                print row


