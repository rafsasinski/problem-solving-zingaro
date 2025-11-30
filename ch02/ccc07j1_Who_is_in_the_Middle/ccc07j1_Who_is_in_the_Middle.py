# https://dmoj.ca/problem/ccc07j1

a = int(input())
b = int(input())
c = int(input())

if (a > b and a < c) or (a < b and a > c):
    print(a)
elif (b > a and b < c) or (b < a and b > c):
    print(b)
else:
    print(c)
