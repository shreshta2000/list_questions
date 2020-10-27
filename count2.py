list1 = [1,2,3,4,5,6,1,4,1,3,1]
i=0
count=0
while i<len(list1):
	j=0
	while j<len(list1):
		if list1[i]==list1[j]:
			count=count+1
			break
		j=j+1
	i=i+1
print(count)