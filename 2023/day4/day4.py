import re
import time
import numpy as np

start_time = time.time()

text = ""
with open("day4.txt") as file:
    text = file.read()

class Card:
    def __init__(self, id,numbers,winning_numbers) -> None:
        self.id = id
        self.numbers = numbers
        self.winning_numbers = winning_numbers
        self.copies = 1

        self.wins = len(np.intersect1d(self.numbers,self.winning_numbers))
        self.score = int(2**(self.wins-1))

        
cards = []
# put all cards in a deck and set properties
for line in text.splitlines():
    id, numbers, winning_numbers = re.findall(r'[^\||:]+',line)

    id = [int(x) for x in re.findall(r'\d+',id)][0]
    numbers = [int(x) for x in re.findall(r'\d+',numbers)]
    winning_numbers = [int(x) for x in re.findall(r'\d+',winning_numbers)]
    cards.append(Card(id, numbers, winning_numbers))

# iterate over the cards
for i in range(len(cards)):
    card = cards[i]

    # add copies of cards that you won
    for j in range(i+1,i+card.wins+1):
        if j > len (cards) - 1:
            break
        cards[j].copies += card.copies


total_points = [x.score for x in cards] # part 1
total_cards = [x.copies for x in cards] # part 2

print("\nSolution part 1 = ",sum(total_points))
print("Solution part 2 = ",sum(total_cards))
print("--- %s millis ---\n" % ((time.time() - start_time) * 1000))
