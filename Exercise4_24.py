rank = random.choice(("Ace",'2','3','4','5','6','7','8','9',"Jack", "King","Queen"))
suit = random.choice(("Clubs", "Diamonds", "Hearts", "Spades"))
card = rank + suit
print("The card you picked is", rank, "of", suit)