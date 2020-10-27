list1=[2,4,6,8]
list2=[4,6,3,8]
if len(list1)<len(list2):
	a=list1
elif len(list1)>len(list2):
	a=list2
else:
	a=list1
i=0
while i<len(a):
	b=list1[i]
	if b==list2[i]:
		print(b)
	i=i+1
