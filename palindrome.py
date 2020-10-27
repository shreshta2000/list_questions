name=[ 'n', 'i', 't', 'i', 'n']
a=len(name)
i=a-1
c=[]
while i>=0:
	c.append(name[i])
	i=i-1																												
if name == c:
	print("it is a palidrome",name)
else:
 	print("it is not a palidrome ",name)
