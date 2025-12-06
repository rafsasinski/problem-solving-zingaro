# https://dmoj.ca/problem/ccc11s1

line_number = int(input())
lines = []

for line in range(0, line_number):
    lines.append(input())

text = " ".join(lines)

char_t = text.upper().count('T')
char_s = text.upper().count('S')

if (char_s >= char_t):
    print("French")
else:
    print("English")
