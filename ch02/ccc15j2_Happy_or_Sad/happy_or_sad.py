# https://dmoj.ca/problem/ccc15j2
message = input()
happy   = message.count(":-)")
sad     = message.count(":-(")

if happy == 0 and sad == 0:
    print("none")
elif happy > sad:
    print("happy")
elif happy < sad:
    print("sad")
else:
    print("unsure")
