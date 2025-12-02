# https://dmoj.ca/problem/wc17c3j3

'''
 - between 8 and 12 chars
 - at lest 3 lower case letters
 - at least 2 upper case letters
 - at last one digit
'''

password = input()

upper = 0
lower = 0
digit = 0

if len(password) >= 8 and len(password) <= 12:
    for ch in password:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        else:
            digit += 1
    
    if lower >= 3 and upper >= 2 and digit >= 1:
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")

print(status)
