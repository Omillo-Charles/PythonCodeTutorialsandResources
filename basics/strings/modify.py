#UPPERCASE
#The upper() method returns the string in upper case
greeting = "hello world"
print(greeting.upper())

#LOWERCASE
name = "OMILLO"
print(greeting.lower())

#REMOVE WHITESPACE
#Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
unit = "Probability and Statistics   "
print(unit.strip()) #Remove any whitespace at the beginning and at the end

#REPLACE STRING
#The replace() method replaces a string with another string
unitName = "Object oriented analysis and design"
print(unitName.replace("and", "with"))

#SPLIT STRINGS
#The split() method splits the string into substrings if it finds instances of the separator
faculty = "Computing and Information Technology"
print(faculty.split("and"))