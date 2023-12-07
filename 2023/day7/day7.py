import re
import time
import numpy as np

start_time = time.time()

input = [*open('input.txt')]
card_order1 = list("23456789TJQKA")
card_order2 = list("J23456789TQKA")

def score(hand,part2):
    if part2:
        card_order = card_order2
        jokers = hand.count('J')
        hand2 = [x for x in hand if not x == 'J']
        c, n = list(np.unique(hand2, return_counts=True))
        zipped = list(zip(c,n))
        sorted_hand = sorted(zipped, key=lambda x: x[1], reverse=True)
        if sorted_hand:
            card, x = sorted_hand[0]
            sorted_hand[0] = (card, x+jokers)
        else:
            sorted_hand = [('J', 5)]
    else:
        card_order = card_order1
        c, n = list(np.unique(hand, return_counts=True))
        zipped = list(zip(c,n))
        sorted_hand = sorted(zipped, key=lambda x: x[1], reverse=True)

    hand_score = sum([(card_order.index(x)+1)*10**(8-i*2) for i,x in enumerate(hand)])
    
    for _,amount in sorted_hand:
        if amount == 5:
            hand_score += 6e12
        elif amount == 4:
            hand_score += 5e12
        elif amount == 3:
            hand_score += 3e12
        elif amount == 2:
            hand_score += 1e12
    return(hand_score)

def calc_total_winnings(part2):
    sorted_input = sorted(input, key=lambda x: score(list(x.split()[0]),part2))

    total_winnings = 0
    hands = []
    for i,hand in enumerate(sorted_input):
        bids = int(hand.split()[1])
        total_winnings += bids*(i+1)
    return total_winnings

print("\nSolution part 1 = ",calc_total_winnings(False))
print("\nSolution part 2 = ",calc_total_winnings(True))
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))