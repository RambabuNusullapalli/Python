from sys import argv
print(type(argv))
print(argv)
print(argv[0])
from sys import argv as a
print(type(a))
print(a[0])
print(a[2])
print(a[-1])
for x in a :
	print(x)
print(" Length of the argument :",len(a))
print(a[1]+a[2])
#print(int(a[1])+int(a[2]))
print(eval(a[1])+eval(a[2]))
print('abc')
print()
print('efg')
print('Hello'+'World')
a,b,c=10,22.22,'ramu'
print(" The information of a,b,c are;",a,b,c)
A='Rambabu'
B='DevOps Engineer'
print(' I am ' , A ,'I am a', B)
print('I am {},I am a {}'.format(A,B))
print('I am {0},I am a {1}'.format(B,A))
print('I am {0},I am a {1}'.format(A,B))
print('I am {1},I am a {0}'.format(B,A))


