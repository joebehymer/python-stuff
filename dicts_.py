# represent student using dictionary
student = {
    'name': 'Joe',
    'age': 25,
    'courses': ['Math', 'CompSci'],
    1: 'intkey'
}

print(student)

# get value of one key
print (student['courses'])
print(student[1]) # keys can be ints too

# throws an error if we try to direct access a key that doesn't exist, so we can use get instead
print(student.get('name'))
print(student.get('phone', 'empty!'))

# add phone to dictionary
student['phone'] = '555-5555'
print(student['phone'])

# add or update things via update method
student.update({'name': 'John', 'phone': '333-3333'})
print(student)

# delete a key and its value
# del student['age'] 
print(student)

# pop removes and returns
print(student.pop('age'))
print(student)

print(len(student))
print(student.keys())
print(student.values())

# looping thru dict
for key, value in student.items():
    print(f'Key={key}. Value={value}')

    