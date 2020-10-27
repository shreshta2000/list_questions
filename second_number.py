list1=[1,2,3,23,24,56,12]
maxi=0
i=0
while i<len(list1):
	if list1[i]>maxi:
		maxi=list1[i]
	i=i+1
	second_max=0
	j=0
	while j<len(list1):
		if maxi>list1[j] and second_max<list1[j]: 
			second_max=list1[j]
		j=j+1
print(second_max)