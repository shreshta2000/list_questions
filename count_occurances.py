char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
while i<len(char_list):
	if char_list[i]=="a":
		a.append(char_list[i])
		j=0
		while j<len(a):
			j=j+1
	if char_list[i]=="n":
		b.append(char_list[i])
		s=0
		while s<len(b):
			s=s+1
	if char_list[i]=="t":
		c.append(char_list[i])
		y=0
		while y<len(c):
			y=y+1
	if char_list[i]=="x":
		d.append(char_list[i])
		z=0
		while z<len(d):
			z=z+1
	if char_list[i]=="u":
		e.append(char_list[i])
		w=0
		while w<len(d):
			w=w+1
	if char_list[i]=="g":
		f.append(char_list[i])
		t=0
		while t<len(f):
			t=t+1
	i=i+1
print(("a",j),("n",s),("t",y),("x",z),("u",w),("g",t))