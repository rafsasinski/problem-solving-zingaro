# https://dmoj.ca/problem/coci17c1p1

deck = ([0] * 2) + [4 for _ in range(8)] + [4*4] + [4]
total_in_hand = 0

N = int(input())
for n in range(N):
    draw_card = int(input())
    deck[draw_card] -= 1
    total_in_hand += draw_card

X = 21 - total_in_hand
left_side = sum(deck[0:X+1])
right_side = sum(deck[X+1:])

if right_side >= left_side:
    print("DOSTA")
else:
    print("VUCI")

'''
Draw cards untill sum(cards) in hand is <= 21 
or says "DOSTA"

52 Cards in the deck, with ranks (points)
 - 11 (Ace)
 - 10 (Jack, Queen, King, 10)
 -  n (number cards values are n, for example card 9 has value 9)

Caesar i in situation
    he has N cards in hand with sum <= 21, he thinks if to draw or not one more card
    
    Assume, X = 21 - sum(N Caesar cards in hand)

    if sum(CARDS IN DECK which VALUE > X) >= sum(CARDS IN DECK which VALUE <= X)
        DO NOT DRAW  cards from the DECK
    else:
        DRAW new card from the DECK

INPUT:
    N - number of cards Caesar drawn so far (1 <= N <= 52)
    Ni - N lines of the value the Caesar drew

OUTPUT:
        "VUCI" - Drawn new card from the deck
        "DOSTA" - Stop no more cards

EXAMPLE
6
2
3
2
3
2
3
OUTPUT
DOSTA

X = 21 - sum(N cards in hand) = 21 - (2+3+2+3+2+3) = 21 - 15 = 6
'''
