# https://dmoj.ca/problem/ccc99s1

DECK_SIZE = 52
deck = []
player_points = [0, 0]

def no_high(lst):
    high_cards = ['ace', 'king', 'queen', 'jack']
    return not any(card in high_cards for card in lst)

for i in range(DECK_SIZE):
    deck.append(input())

for i in range(DECK_SIZE):
    card = deck[i]
    player_id = i%2

    remaining = DECK_SIZE - (i + 1)
    points = 0

    if card == "ace" and remaining >= 4:
        if no_high(deck[i+1:i+5]):
            points = 4
    elif card == "king" and remaining >= 3:
        if no_high(deck[i+1:i+4]):
            points = 3
    elif card == "queen" and  remaining >= 2:
        if no_high(deck[i+1:i+3]):
            points = 2
    elif card == "jack" and  remaining >= 1:
        if no_high(deck[i+1:i+2]):
            points = 1

    if points > 0:
        player_points[player_id] += points
        print(f"Player {"B" if player_id else "A"} scores {points} point(s).")

for i in range(len(player_points)):
    print(f"Player {"B" if i%2 else "A"}: {player_points[i%2]} point(s).")