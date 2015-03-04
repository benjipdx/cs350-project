#! /usr/bin/env python
from InputGenerator import inputGenerator
from HashTable import HashTable
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

        self.test_strings =  random.sample(self.random_strings, count) #how random is this?
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

def restoreInput(filename):
    import pickle
    f = open(filename, "rb")
    tmp = pickle.load(f)
    f.close()
    return tmp

#-----TEST 1-----#
def test(searchcount,invalidcount,stringcount):

        #now run this
        w = Worker()
        search_item_count = searchcount
        invalid_item_count = invalidcount
        string_count = stringcount
        w.build(string_count,search_item_count,invalid_item_count)

        #Save input to pickle file
        import time,pickle
        datadir = "data"
        filetime = str(int(time.time()))
        inputfilename = datadir+"/"+filetime+"/"+"input-"+filetime
        import os
        if not os.path.exists(os.path.dirname(inputfilename)):
            os.makedirs(os.path.dirname(inputfilename))

        inputfile = open(inputfilename,"w+")
        pickle.dump(w,inputfile)
        inputfile.close()

        #restore = restoreInput(inputfilename)

        trial_count = 10

        #------HASH TABLE------#
        #now we insert
        print("Adding items to hash table....")
        h = HashTable(57)
        import sys
        import time

        datafilename = datadir+"/"+filetime+"/"+"HT-"+filetime+".csv"        
        import os
        if not os.path.exists(os.path.dirname(datafilename)):
          os.makedirs(os.path.dirname(datafilename))
        datafile = open(datafilename,"wb+")
        #prep data file
        datafile.write("HashTable-"+filetime+"-Insert\n")
        datafile.write("Trial,N,BasicOps,Time\n")
        
        for trial in range(trial_count):
          datafile.write(str(trial)+",")

          basicop = 0
          begintime = time.time()
          for i in w.random_strings:
            basicop+=h.add(i)
          endtime = time.time()
          diff = endtime - begintime
          datafile.write(str(stringcount)+",")
          datafile.write(str(basicop)+",")
          datafile.write(str(diff)+"\n")
          print("insert time: %s" % diff)
          print("basic op count: %s" % basicop)

        datafile.close()

        #-----BST--------------#



        #-----234treeeeeeeeeee--------------#


test(1000,1000,10000)


