list1=[5,2,3,9]
i=0
greatest=0
lowest=list1[0]
a=[]
while i<len(list1):
	if list1[i]>greatest:
		greatest=list1[i]
	if list1[i]<lowest:
		lowest=list1[i]
	i=i+1
low=(lowest)
large=(greatest)
while low<=large:
	if low not in list1:
		print(low)
	low=low+1