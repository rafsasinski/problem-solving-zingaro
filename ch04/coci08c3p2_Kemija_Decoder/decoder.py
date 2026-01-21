'''
vovels:
    aeiou

ENCODER
After each vovel add p + vovel
    kemija -> kepemipijapa

Task:
Write a DECODER
    kepemipijapa -> kemija
'''

VOVELS = "aeiou"
encoded = input()
decoded = ""


i = 0
while i < len(encoded):
    ch = encoded[i]
    decoded += ch
    
    if ch in VOVELS:
        i += 3
    else:
        i += 1

print(decoded)
