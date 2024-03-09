# Ask user for their name
name = input("What's your name? ")

# Remove whitespaces from str and capitalize user's name
name = name.strip().title()



# Diffrent ways to say hello to user
#In one line
print("hello, " + name)
print("hello,", name)
print(f"hello, {name}")

#In two lines
print("hello, ", end="")
print(name)

#how to use quatations
print('hello, "friend"')
print("hello, \"friend\"")