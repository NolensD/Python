'''
Created on Dec 14, 2018

@author: Win7LocalAdmin
'''
#===============================================================================
# def power(x, y=2):
#     r = 1
#     for _ in range(y):
#         r = r*x
#     return r
# 
# 
# print(power(3))
# print(power(3, 3))
#===============================================================================

#===============================================================================
# list_2d = [[1,2,3], [4,5,6], [7,8,9]]
# 
# 
# for i in range(1,3):
#     for j in range(-2,0):
#         print(list_2d[i][j], end='')
#===============================================================================

#===============================================================================
# test = [11, 22, 33, 21, 10]
# 
# 
# result = test[0]
# for iter in test:
#     if iter > result:
#         result = iter
# 
# 
# print(result)
#===============================================================================

#===============================================================================
# ints = tuple([1,1,2,3,3,3,4])
# print(len(ints))
#===============================================================================

#===============================================================================
# x = 50
# 
# 
# def func(x):
#     print('this x is', x)
#     x = 2
#     print('but this x is', x)
# 
# 
# func(x)
# print('x is', x)
#===============================================================================

#===============================================================================
# a = list('Python Rocks!!')
# for i in range(5):
#     a.pop(1)
#     
# print(a)
#===============================================================================

#===============================================================================
# s = '024681012'
# print(s[-2:-8:-2])
#===============================================================================

#===============================================================================
# def my_func(a, b):
#     return a[:b]
# 
# print(my_func('Notebook', 5))
#===============================================================================

#===============================================================================
# for i in range(10):
#     if i%2==0:
#         continue
#     if i==6:
#         break
#     print(i)
#===============================================================================

#===============================================================================
# a, b = 0,1
# for i in range(0,10):
#     print(a, end=' ')
#     a, b = b, a+b
#===============================================================================

x = ['ab', 'cd']


for i in x:
    i.upper()


print(x)