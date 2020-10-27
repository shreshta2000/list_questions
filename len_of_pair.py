list1=[1,3,2,1,2,1]
i=0
a=[]
count=0
# while i<len(list1):
# 	j=0
# 	while j<len(list1):
# 		# if list1[i] not in a:
# 		# 	a.append(list1[i])
# 		if list1[i]==list1[j]:
# 			count=count+1
# 		j=j+1
# 	i=i+1
# print(count)
i=0
while i<len(list1):
	j=0
	while j<=i:
		if list1[i]==list1[2]:
			a.append(list1[j])
			count=count+1
		j=j+1
	i=i+1
print(a)


