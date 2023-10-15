import random 

coin = random.choice(["heads","tails"])


cards = ["1","2","3"]
random.shuffle(cards)

for card in cards:
    print(card)
    