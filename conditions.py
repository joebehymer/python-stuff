lang = 'Python'
user = 'Admin'
loggedin = False
# if lang == 'Python':
#     print(True)
# else:
#     print(False)

# if lang is lang2: # checks if they are the same pointer
    # print('lang is lang2')

# elif is basically a switch/case
# if lang == 'Java':
#     print('Java')
# elif lang == 'Python':
#     print('Python')
# else:
#     print('no match')

if user == 'Admin' or loggedin:
    print('Admin Page')
else:
    print('Regular Page')

if not loggedin:
    print('Please log in..')
else:
    print('Logged in!')