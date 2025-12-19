# https://dmoj.ca/problem/ccc19j3

n = int(input())

while n:
    n = n - 1
    line = input()
    encoded = ""

    # START: Encode line
    occurrence = 0
    for i in range(len(line)):
        ch = line[i]
        occurrence = occurrence + 1

        if i == len(line) - 1 or ch != line[i+1]:
            encoded = encoded + f"{occurrence} {ch} "
            occurrence = 0
    # END: Encode line

    print(encoded.strip())



'''
Run-length encoding
For each symbol, write down number of times it appears consecutively,
followed by the symbol itself.

INPUT:
    N - number of lines to encode, for example:

    2
    +++===!!!!
    rs

OUTPUT:
    3 + 3 = 4 !
    1 r 1 s
'''
