import bisect
import random
size=7
random.seed(1729)
my_list=[]
for i in range(size):
    new_item=random.randrange(size*2)
    bisect.insort(my_list,new_item)
    print('%2d->'%new_item,my_list)