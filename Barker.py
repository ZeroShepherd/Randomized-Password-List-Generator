import random
import re
import sys
import os

newpath = r"/home/zero/Desktop/"
if not os.path.exists(newpath):
    os.makedirs(newpath)

orig_stdout = sys.stdout
f = open("/home/zero/Desktop/dictionary.txt", 'w')
sys.stdout = f
howManyLength = 14
howManyPrints = 999999999

lower_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

all = []
all = lower_a + num

for r in range(howManyPrints):
    subThis = (str(random.choices(all, k=howManyLength)))
    print(re.sub('\'|\,|\[|\]|\ ', '', subThis))



sys.stdout = orig_stdout
f.close()
