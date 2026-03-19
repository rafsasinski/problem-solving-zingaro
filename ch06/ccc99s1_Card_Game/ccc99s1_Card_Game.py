# https://dmoj.ca/problem/ccc99s1

DECK_SIZE = 52
HIGH_CARDS = ['ace', 'king', 'queen', 'jack']
POINTS_MAX = 4
deck = []
player_points = [0, 0]

for i in range(DECK_SIZE):
    deck.append(input())

for i in range(DECK_SIZE):
    card = deck[i]
    player_id = i%2

    remaining = DECK_SIZE - (i + 1)

    if card in HIGH_CARDS:
        points = 0
        if card == "ace" and remaining >= 4:
            if not any(card in HIGH_CARDS for card in deck[i+1:i+5]):
                points = POINTS_MAX - HIGH_CARDS.index(card)
        elif card == "king" and remaining >= 3:
            if not any(card in HIGH_CARDS for card in deck[i+1:i+4]):
                points = POINTS_MAX - HIGH_CARDS.index(card)
        elif card == "queen" and  remaining >= 2:
            if not any(card in HIGH_CARDS for card in deck[i+1:i+3]):
                points = POINTS_MAX - HIGH_CARDS.index(card)
        elif card == "jack" and  remaining >= 1:
            if not any(card in HIGH_CARDS for card in deck[i+1:i+2]):
                points = POINTS_MAX - HIGH_CARDS.index(card)

        if points > 0:
            player_points[player_id] += points
            print(f"Player {"B" if player_id else "A"} scores {points} point(s).")

for i in range(len(player_points)):
    print(f"Player {"B" if i%2 else "A"}: {player_points[i%2]} point(s).")