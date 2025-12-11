#Variables are containers for storing data
#Python has no command for declaring a variable.A variable is created the moment you first assign a value to it.
#Variable names are case-sensitive.
number = 5
name = "John Doe"
print(number)
print(name)

#CASTING
#If you want to specify the data type of a variable, this can be done with casting.
admNumber = str(213232) #outputs '213232'
regNumber = int(783278372) #outputs 783278372
unitPoints = float(365362532) #outputs 365362532.0

#GETTING THE TYPE
#You can get the data type of a variable with the type() function.
firstName = "Omillo"
age = 20
print(type(name)) #outputs str
print(type(age)) #outputs int

#ASSIGNING MULTIPLE VALUES
a, b, c = "Omillo", "Fidel", "Charles"
print(a) #Omillo
print(b) #Fidel
print(c) #Charles

#And you can assign the same value to multiple variables in one line

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["Mango", "Orange", "Apple"]
e, f, g = fruits
print(e) #Mango
print(f) #Orange
print(g) #Apple