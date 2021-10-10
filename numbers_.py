
# int and float types
num = 3.14
print(type(3))
print(type(3.15))

print (3/2) # used to drop decimal, now returns float

# floor division (chop off decimal)
print(3//2)

# exponent 3^4
print(3**4)

#mod (eg: used to tell if even or odd)
print(3%2)

# order of operations
print (3 * 2 + 1)
print (1 + 3 * 2)
print (3 * (2+1))

# increment
num = 1
num *= 10
print(num)

# built in number functions
print (abs(-15))
print (abs(-3.4))
print (round(3.45, 1))
print (round(3.45, 2))

# comparisons return booleans
num_1 = 3
num_2 = 2
print (num_1 == num_2)
print (num_1 != num_2)
print (num_1 >= num_2)

# strings and numbers
num_1 = '100'
num_2 = '200'
print(int(num_1) + int(num_2))