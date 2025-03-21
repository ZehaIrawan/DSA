import random

# 1. Creating deck
# First list the ranks and suits
# Then generate the deck of 52 cards
# Generating random cards doesn't account of possible duplicates
# To generate the deck you will need each ranks for each suits, for loop is perfect

# 2. Picking cards from the deck
# After you have the deck, you need to pick random card and remove it from deck

def create_deck():
  ranks = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']

  suits = ['Spades','Hearts','Diamonds','Clubs']

  deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]

# This is equivalent of writing
# deck = []
# for suit in suits:
#     for rank in ranks:
#         deck.append(f"{rank} of {suit}")
  return deck



def draw_cards(deck,n):
  if len(deck) < n:
    return 'Not enough cards in the deck!'

  return [deck.pop() for _ in range(n)]
# https://www.w3schools.com/python/python_lists_comprehension.asp
#  list comprehension that efficiently removes and returns n cards from the deck.
# _ is a throwaway variable (since we don't need its value).
# deck.pop() removes and returns the last card from deck.
# The list comprehension collects these popped cards into a list.

# Generate and shuffle the deck
deck = create_deck()

# Without shuffle it will always pick the same cards
# random.shuffle(deck)

# Draw 5 cards
hand = draw_cards(deck, 10)
print(f"Drawn cards: {hand}")
print(f"Remaining cards in deck: {len(deck)}")




