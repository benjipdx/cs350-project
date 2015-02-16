# cs350-project
PSU Algorithms &amp; Complexity term project of Black's cs350 Winter term class

# print random string
import string
import random
print(''.join(random.choice(string.ascii_uppercase) for i in range(12)))
