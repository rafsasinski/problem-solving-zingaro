# https://dmoj.ca/problem/ccc18j1

number = []

number.append(int(input()))
number.append(int(input()))
number.append(int(input()))
number.append(int(input()))

if ((number[0] == 8 or number[0] == 9) and
    (number[3] == 8 or number[3] == 9) and
    (number[1] == number[2])):
    print("ignore")
else:
    print("answer")
