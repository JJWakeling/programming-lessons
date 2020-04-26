#function with a side-effect
def greet(name):
	print("Hello, " + name)

#function returning a value
def greeting(name):
	return "Hello, " + name
	
name = "Joe"
greet(name)
print(greeting(name))