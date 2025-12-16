# https://dmoj.ca/problem/coci08c3p2

encoded = input()
decoded = ""
i = 0

while i < len(encoded):
    ch = encoded[i]

    if ch in 'aeiou' and encoded[i+1] == "p" and encoded[i+2] == ch:
        decoded = decoded + ch
        i = i + 3
    else:
        decoded = decoded + ch
        i = i + 1


print(decoded)
