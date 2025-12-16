# https://dmoj.ca/problem/coci08c3p2

encoded = input()
decoded = ""
i = 0

while i < len(encoded):
    ch = encoded[i]

    if ch in 'aeiou':
        i = i + 3
    else:
        i = i + 1

    decoded = decoded + ch

print(decoded)
