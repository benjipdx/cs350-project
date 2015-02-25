#! /usr/bin/env python
from InputGenerator import inputGenerator
import random

class Worker():
    def __init__(self):
        self.random_strings = []
        self.gen = inputGenerator()
        self.test_strings = []
        self.error_strings = []

    def genStrings(self,count):
        """makes a list of strings for later use"""
        self.random_strings = self.gen.make(count) #generates 5000 unique strings
        return

    def cherryPick(self,count):
        """returns list of indices of random selected for testing"""
        #for i in range(count):
        #    random_list.append(random.randint(1,stringcount))

        self.test_strings =  random.sample(self.random_strings, count)
        return

    def genErrorString(self):
       
        gen_string = self.gen.generateString()
        while(gen_string in self.random_strings):
            #try again
            gen_string = self.gen.generateString()

        #now we have the string we want
        return gen_string

    def genErrorStringList(self,count):
        for i in range(count):
            tmp = self.genErrorString()
            self.error_strings.append(tmp)

        return

    def build(self,string_count,valid_test_count,invalid_test_count):
        self.genStrings(string_count)
        self.cherryPick(valid_test_count)
        self.genErrorStringList(invalid_test_count)
        return


#now run this
w = Worker()
search_item_count = 20
invalid_item_count = 20
string_count = 5000
w.build(string_count,search_item_count,invalid_item_count)


#some timeit shit here
#now we insert
#for i in 



