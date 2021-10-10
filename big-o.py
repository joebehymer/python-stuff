# permutations of a string


def permutation(str: str, prefix = ""):
    if (len(str) == 0):
        print(prefix)
    else:
        for i, char in enumerate(str):
            remaining = str[0:i] + str[i + 1:len(str)]
            permutation(remaining, prefix + str[i]) 


permutation("JoeB")