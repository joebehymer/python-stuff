
backing = {}
backing[0] = 0
backing[1] = backing[2] = 1
def fibDynamic(n):
    if n in backing: return backing[n]

    i = 3
    while (i <= n):
        backing[i] = backing[i-1] + backing[i-2]
        i += 1
    return backing[n]

def fibRecursive(n):
    if (n == 1 or n == 2): return 1
    return fibRecursive(n-1) + fibRecursive(n-2)

# print(fibRecursive(6))

def testFib():
    outputs = [1,1,2,3,5,8,13,21,34,55]

    for input in range(1, 11):
        val = fibDynamic(input)
        if val == outputs[input-1]: 
            print (f'fibRecursive passed!  fib({input}) == {val}')
        else:
            print (f'fibRecursive failed!  fib({input}) != {val}')

testFib()