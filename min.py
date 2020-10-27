numbers=[23,43,12,3]
min=numbers[0]
i=0
while i < len(numbers):
	if numbers[i]<min:
		min=numbers[i]
	i=i+1
print(min)