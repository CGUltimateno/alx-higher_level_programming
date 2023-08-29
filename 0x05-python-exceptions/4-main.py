#!/usr/bin/python3

list_divide = __import__('4-list_division.py').list_division

l1 = [10, 8, 4]
l2 = [2 , 4, 4]

res = list_divide(l1, l2, max(len(l1)), max(len(l2)))
print(res)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
res = list_divide(my_l_1, my_l_2, max(len(l1), len(l2)))
print(res)
