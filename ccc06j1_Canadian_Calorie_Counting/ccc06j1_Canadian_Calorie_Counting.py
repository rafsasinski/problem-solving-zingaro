# https://dmoj.ca/problem/ccc06j1

burgers = [461, 431, 420, 0]
sides = [100, 57, 70, 0]
drinks = [130, 160, 118, 0]
desserts = [167, 266, 75, 0]

total = burgers[int(input()) - 1]
total += sides[int(input()) - 1]
total += drinks[int(input()) - 1]
total += desserts[int(input()) - 1]

print(f"Your total Calorie count is {total}.")
