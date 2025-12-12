#Strings in python are surrounded by either single quotation marks, or double quotation marks.
name = "Omillo Fidel Charles"
print(name)
print("Omillo Fidel Charles")

#Multiline strings
randomText = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

#strings are arrays
unit = "Probability"
print(unit[2])

#Looping through a string
for i in unit:
    print(i)

#String length
greeting = "Hello World"
print(len(greeting))

#Check string
text = "London is blue!"
print("is" in text)