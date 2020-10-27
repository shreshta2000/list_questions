list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
i=0
a=[]
sum=0
while i<len(list1):
	sum=list1[i]+list2[i]
	a.append(sum)
	i=i+1
print(a)