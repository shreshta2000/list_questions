list1=[2,4,6,8]
list2=[4,6,3,8]
if len(list1)<len(list2):
	a=list1
elif len(list1)>len(list2):
	a=list2
else:
	a=list1
sum=0
i=0
while i<len(a):
	sum=list1[i]+list2[i]
	print(sum)
	i=i+1
