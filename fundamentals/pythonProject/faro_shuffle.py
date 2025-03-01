# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half.
# Then the cards in the two halves are perfectly interleaved, such that the original bottom card is still on the bottom and the original top card is still on top.
#
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six']
#
# Write a program that receives a single string (cards separated by space) and on the second line receives a count of faro shuffles that should be made.
# Print the state of the deck after the shuffle.
#
# Note: The length of the deck of cards will always be an even number.

deck_of_cards = input().split()
faro = int(input())

for current_shuffle in range(faro):
    middle = len(deck_of_cards) // 2
    left = deck_of_cards[:middle]
    right = deck_of_cards[middle:]
    shuffled_deck = []

    for index in range(len(right)):
        shuffled_deck.append(left[index])
        shuffled_deck.append(right[index])

    deck_of_cards = shuffled_deck.copy()

print(deck_of_cards)