a=[20,30,40,20.34,'Ramu',True]
print(a)
a.append("Rambabu")
print(a)
a.append(34)
print(a)
a.remove(30)
a.append(40)
a.append(40)
print(a)
print(a[2])
print(a[-1])
print(type(a))
print(a)
b=(20,30,40,20.34,'Ramu',True)
print(b)
print(b[-1])
print(b[4])
# b.append(23)
print(b)
print(type(b))
# set
c={20,30,40,20.34,'Ramu',True}
print(c)
# print(c[4])
c.add(67)
print(c)
c.add("Rambabu")
print(c)
c.add(True)
print(c)
c.remove(20)
#c.remove(2)
print(c)
print(type(c))
d=frozenset(c)
print(d)
# d.add(23)
#d.remove(22)
# print(d[2])
print(type(d))
print(d)







