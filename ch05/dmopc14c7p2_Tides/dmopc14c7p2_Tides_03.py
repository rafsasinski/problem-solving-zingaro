def getExtremeIndices(array):
    smallest_index = array.index(min(array))
    largest_index = array.index(max(array))
    return (smallest_index, largest_index)

def sliceDaList(array, fromto):
    return array[fromto[0]:fromto[1]+1]
    
def checkListIsIncremental(array):
    if len(array) <= 1:
        return False

    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            return False

    return True


dataset = int(input())
for _ in range(dataset):
    N = int(input())
    measurements = [int(i) for i in input().split()]
    extremeIndices = getExtremeIndices(measurements)

    slicedMeasurements = sliceDaList(measurements, extremeIndices)

    listIsIncremental = checkListIsIncremental(slicedMeasurements)

    if listIsIncremental:
        value_min = measurements[extremeIndices[0]]
        value_max = measurements[extremeIndices[1]]
        print(value_max - value_min)
    else:
        print("unknown")
