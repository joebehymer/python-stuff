message = 'Hello World'
print(message)

# how many chars in the string?
print ("Length= " + str(len(message)))

# access chars
print(message[10])

# string slicing, just get hello
print(message[:5])

# subset, just get world
print(message[6:])

# lower case message
print(message.lower())

# count chars
print(message.count('l'))

# find index
print(message.find('World'))

# replace chars
message2 = message.replace('World', 'Universe')
print(message2)

# concat strings together
greeting = 'Hello'
name = 'Joe'
message = greeting + ', ' + name + '. Welcome!'
print(message)

# format strings
message = '{}, {}. Welcome!'.format(greeting, name)

# new f strings in 3.6 or above
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

# print autocomplete
#print(dir(message))
#print(help(str))
# print(help(str.lower))
