
import string
import random
 
# initializing size of string
N = 7
 
# using random.choices()
# generating random strings
letters = string.ascii_lowercase
print(( ''.join(random.choice(letters) for i in range(10)) ))
print(( ''.join(random.choice(letters) for i in range(10)) ))
print(( ''.join(random.choice(letters) for i in range(10)) ))
print(( ''.join(random.choice(letters) for i in range(10)) ))
i = 0
while i<35:
    print(i)
    i=i+1
