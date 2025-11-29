# https://dmoj.ca/problem/ccc18j1

number = []

number.append(int(input()))
number.append(int(input()))
number.append(int(input()))
number.append(int(input()))

if number[0] in (8, 9) and number[3] in (8, 9) and number[1] == number[2]:
    print("ignore")
else:
    print("answer")
