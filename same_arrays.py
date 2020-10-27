list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
# i=0
# a=[]
# c=len(list1)
# while i<c:
# 	b=list1[i]
# 	j=0
# 	while j<len(list2):
#  		if list2[j] ==  list1[i]:
#  			a.append(list2[j])
		
# 	 	j=j+1
# 	i=i+1
# print(a)
i=0
a=[]
while i<len(list1):
	if list1[i] not in list2:
		print(list1[i])
		a.append(list1[i])
	i=i+1
print(a)