# https://dmoj.ca/problem/ccc00s2

N = int(input())
flows = []
for _ in range(N):
    flows.append(int(input()))

line = input()

while line != "77":
    stream = int(input()) - 1

    if line == "99":
        # SPLIT
        percentage = int(input())
        stream_value = flows[stream]
        flows[stream] = round(stream_value * percentage/100)
        flows.insert(stream+1, round(stream_value * (100-percentage)/100))
    elif line == "88":
        # JOIN
        if stream == 0:
            flows = [flows[0] + flows[1]] + flows[2:]
        else:
            flows = flows[0:stream] + [flows[stream] + flows[stream+1]]
    
    line = input()

print(" ".join([str(val) for val in flows]))

'''
NOTES:
at any given elevation there are M streams, 1 to m from ltr
stream may split into a left fork and a right fork (M += 1)
(1 <= M <= 100)

INPUT
N - number of steams at altitue
Nlines - of FLOW in each of the stream (ltr)

SPLIT
99 - SPLIT indication
s - number of stream that is split
p - (0 <= p <= 100) precentage of flow on the left fork

JOIN
88 - JOIN indication
r - number of stream that is jined with stream to its RIGHT
The flow from both joined streams is combined

END OF INPUT
77
'''
