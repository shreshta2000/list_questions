list1=[1,2,50,543,56,43,0]
max=0
i=0
while i<len(list1):
	if list1[i]>max:
		max=list1[i]
	i=i+1
print(max)