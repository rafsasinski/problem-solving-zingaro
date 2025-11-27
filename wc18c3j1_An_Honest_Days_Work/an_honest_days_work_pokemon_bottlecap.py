# https://dmoj.ca/problem/wc18c3j1
paint_litres = int(input())
litre_per_cap = int(input())
cap_to_pokedollar = int(input())

caps_produced = paint_litres//litre_per_cap
paint_litres = paint_litres - (caps_produced * litre_per_cap)

total = (caps_produced * cap_to_pokedollar) + paint_litres

print(total)
