import module as m
print(m.sum(3,4))
print(m.sub(10,5))
#print(module.mul(5,6))
from module import sum,sub,mul
print(sum(2,2))
print(sub(10,10))
print(mul(4,4))
from module import *
print(sum(7,2))
print(sub(16,10))
print(mul(7,4))