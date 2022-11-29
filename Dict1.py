 #   Dictionary
c={ 4:"read", 2:"Write" , 1: "Execute"}
print(c)
print(type(c))
d={}
print(d)
print(type(d))
d['u']="Owner"
d['g']="Group"
d['o']="Others"
print(d)
e={}
e[1]='exec'
e[2]='write'
e[3]='ex+wr'
e[0]='null'
e[4]='read'
e[5]='re+ex'
e[6]='re+wr'
e[7]='re+wr+ex'
print(e)
e[1]='exec'   # Keys does not allow repeat
e[2]='write'
print(e)
e[8]='exec'  # Vlaues can be repeated
print(e)
e[9]='exec'
print(e)