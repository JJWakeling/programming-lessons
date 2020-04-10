bool = True
if bool:
	print("bool is true")
	
otherbool = False
if otherbool:
	print("true")
else:
	print("false")
	
value = int(input("enter a number: "))
if value < 5:
	print("small number")
elif value < 20:
	#n.b. you can have as many elif clauses as you like in an if statement
	print("medium size number")
else:
	print("big number")
