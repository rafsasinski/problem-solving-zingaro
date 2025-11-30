# https://dmoj.ca/problem/dmopc16c1p0

pizza_width = int(input())
cheese_coverage = int(input())

if pizza_width == 3 and cheese_coverage >= 95:
    satisfaction = "absolutely"
elif pizza_width == 1 and cheese_coverage <= 50:
    satisfaction = "fairly"
else:
    satisfaction = "very"

print(f"C.C. is {satisfaction} satisfied with her pizza.")
