# Ask user for their name
name = input("What's your name? ")

# Diffrent ways to say hello to user
#In one line
print("hello, " + name)
print("hello,", name)
print("hello," , name, sep="")

#In two lines
print("hello, ", end="")
print(name)