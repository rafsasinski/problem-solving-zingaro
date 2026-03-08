# https://dmoj.ca/problem/dmopc14c7p2
N = int(input())
measurements = [int(i) for i in input().split()]

bad = True 
previous = None

for i in range(N):
    measurement = measurements[i]
    print(f"measurement: {measurement}")

    if previous:
        print("previous")
        if previous > measurement:
            print("previous > measurement")
            print("break")
            break
        previous = measurement

    if measurement == min(measurements):
        print("m == min(ms)")
        previous = measurement
        bad = True
    elif measurement == max(measurements):
        print("m == max(ms)")
        bad = False


if bad:
    print("unknown")
else:
    print(max(measurements) - min(measurements))

'''
1 2 3
2

1 3 2
unkonw
213
2

321
unknown
'''
