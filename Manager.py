#! /usr/bin/env python
from InputGenerator import inputGenerator as generator

random_strings = generator()
random_strings = random_strings.make(5000)
print random_strings
