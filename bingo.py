#coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
GREEN   = '\033[92m'
BLUE    = '\033[94m'
ENDC    = '\033[0m'

import random

l = list(range(1,76))
#print(l)

random.shuffle(l)
#print(l)

def search():
	#print("search")
	num = input("please input number\n---->")
	
	if int(num) in done:
		print("already show")
	else:
		print("Not yet")
	
done = []
for i in l:
	print("\n\n")
	print(GREEN + str(i) + ENDC)
	done.append(i)
	
	flag = input("Please input 1,2 or 3\n1:Run\n2:search\n3:exit\n---->")
	
	if flag == "1":
		continue
	elif flag == "2":
		search()
	else:
		print("Terminate")
		breaki
