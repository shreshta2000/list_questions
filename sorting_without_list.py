list1 = [5,1,4,2,8,3,1]
i = 0
while i < len(list1):
    j = 0 
    while j < len(list1):
        if list1[i] < list1[j]:
            a = list1[i]
            b = list1[j]
            list1[i] = b
            list1[j] = a
        # else:
            # a = list1[i]
            # b = list1[j]
            # list1[i] = b
            # list1[j] = a
        j = j + 1
    i = i + 1
print(list1)

