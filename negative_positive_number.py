list1=[12,23,12,35,67,-2,0,-4,5]
i=0
while i < len(list1):
	if list1[i]<0:
		print("it is a positive no" ,list1[i])
	elif list1[i]==0:
		print("it is a zero",list1[i])
	else:
		print("it is a negative no" ,list1[i])
	i=i+1