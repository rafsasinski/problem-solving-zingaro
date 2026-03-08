dataset = int(input())
print(dataset)
for _ in range(dataset):
    N = int(input())
    measurements = [int(i) for i in input().split()]
    orig = measurements

    smallest = min(measurements)
    largest = max(measurements)
    bad = False


    previous = smallest
    measurements = measurements[measurements.index(min(measurements)):measurements.index(max(measurements))+1]
    if len(measurements) != 0:
        for i in range(measurements.index(smallest)+1, len(measurements)):
            if measurements[i] < previous:
                bad = True
            previous = measurements[i]
    else:
        bad = True;
            

    if bad:
        print("unknown")
    else:
        count = largest - smallest
        print(count)
