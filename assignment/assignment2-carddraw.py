import requests
from collections import Counter

# Shuffle new deck
shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
shuffle_response = requests.get(shuffle_url).json()
deck_id = shuffle_response["deck_id"]

# Draw 5 cards
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
draw_response =requests.get(draw_url).json()
cards = draw_response["cards"]

print("Drawn Cards: ")
values = []
suits = []

for card in cards:
    value = card["value"]
    suit = card["suit"]
    values.append(value)
    suits.append(suit)
    print(f"{value} of {suit}")

# Check for pairs or triples
value_counts = Counter(values)
pair = 2 in value_counts.values()
triple = 3 in value_counts.values()

# Check for flush
flush = len(set(suits)) == 1

# Check for straight
value_map = {
    "ACE": 1, "JACK": 11, "QUEEN": 12, "KING": 13
}

numbers = []
for v in values:
    numbers.append(int(v) if v.isdigit() else value_map[v])

numbers.sort()
straight = all(numbers[i] + 1 == numbers[i + 1] for i in range (4))

print ("\nResults:")
if pair:
    print("Congratulations! You drew a pair.")
if triple:
    print("Congratulations! You drew a triple.")
if straight:
    print("Congratulations! You drew a straight.")
if flush:
    print("Congratulations! All cards are the same suit.")

if not(pair or triple or straight or flush):
    print("No special hand drawn.Better luck next time!")