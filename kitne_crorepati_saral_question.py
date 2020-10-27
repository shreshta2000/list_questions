kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
a=[]
b=[]
c=[]
count=0
while i<len(kitna_paisa_hai):
	if kitna_paisa_hai[i]>=10000000:
		a.append (kitna_paisa_hai[i])
		j=0
		while j<len(a):
			j=j+1
		
	if kitna_paisa_hai[i]>=100000 and kitna_paisa_hai[i]<10000000:
		b.append(kitna_paisa_hai[i])
		x=0
		while x<len(b):
			x=x+1
		
	if kitna_paisa_hai[i]>=0 and kitna_paisa_hai[i]<100000:
		c.append(kitna_paisa_hai[i])
		y=0
		while y<len(c):
			y=y+1
		
	i=i+1
print(j,"crorepati")
print(x,"lakhpati")
print(y,"dilwale")


