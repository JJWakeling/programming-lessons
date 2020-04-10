import random

print("I will now print 10 random numbers between 1 and 5 inclusive")
i = 0
while i < 10:
    print(random.randint(0, 5))
    i += 1
