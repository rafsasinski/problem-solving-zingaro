# https://dmoj.ca/problem/wc18c3j1
paint = int(input())
paint_per_cap = int(input())
dollars_per_cap = int(input())

caps_produced = paint//paint_per_cap
paint = paint - (caps_produced * paint_per_cap)

total = (caps_produced * dollars_per_cap) + paint

print(total)
