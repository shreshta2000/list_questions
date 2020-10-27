Question="What is the capital of India?"
option=["delhi","bhopal","chennai","chandigharh"]
answere="delhi"
print("Q.1",Question)
j=0
while j<len(option):
	print(j+1,option[j])
	j=j+1
your_answere=input("enetre your answere ")
i=0
while i<len(option):
	if your_answere==answere:
		print("your ans is correct")
		print("your next question is")
		Question_2="How many continents are there?"
		option_2=["Four", "Nine", "Seven", "Eight"]
		answere_2="seven"
		print("Q.2",Question_2)
		z=0
		while z<len(option_2):
			print(z+1,option_2[z])
			z=z+1
		your_answere_2=input("entre your answere  ")
		a=0
		while a<len(option_2):
			if your_answere_2==answere_2:
				print("your answere is correct")
				print("your next Question is")
				Quetion_3="NG mei kaun se course padhaya jaata hai?"
				option_3=["Software Engineering", "Counseling", "Tourism", "Agriculture"]
				answere_3="software engineering"
				print("Q.3",Quetion_3)
				c=0
				while c<len(option_3):
					print(c+1,option_3[c])
					c=c+1
				your_anwere_3=input("entre your answere ")
				b=0
				while b<len(option_3):
					if your_anwere_3==answere_3:
						print("your answere is correct")
						break
					else:
						print("your answere is incorrect")
						break
					b=b+1
				break
			else:
				print("your answere is incorrect")
				a=a+1
		break
	else:
		print("your ans is incorrect" )
		break
	i=i+1


