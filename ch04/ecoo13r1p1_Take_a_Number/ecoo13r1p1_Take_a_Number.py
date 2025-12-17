# https://dmoj.ca/problem/ecoo13r1p1

'''
INPUT:
    - N (0 < N < 1000) - next number in THE TAKE A NUMBER MACHINE
    - Lines (up to 1 000 000) of activities at the attendance desk.
        - TAKE - student arrived and take next number
        (if student takes the last number available, machine is refilled)
        - SERVE - secretary served the next student in line
        (only if one student is waiting this will appear)
        - CLOSE - desk is closed for the day, secretary will serve remaining students in line
        - EOF - end of lines

OUTPUT:
    Three integers on a single line (sep. by space):
    - number of students wo were late that day
    - students who rmained in line after desk was closed
    - next number inthe take a number machine for the next day
3 0 26
3 2 29
8 5 37

'''

MAX_NUMBER = 999
number = int(input())

late = 0
line = 0

activity = ''

while activity != 'EOF':
    activity = input()

    if activity == 'CLOSE':
        print(f"{late} {line} {number}")
        late = 0
        line = 0
    elif activity == 'TAKE':
        # (0 < number < 1000)
        if number == MAX_NUMBER:
            number = 0
        number = number + 1
        late = late + 1
        line = line + 1
    elif activity == 'SERVE':
        line = line - 1
