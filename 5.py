cards = input().split()
shuffles_count = int(input())

cards_left = []
cards_right = []

for card in range(shuffles_count):
    cards_list = []
    middle = len(cards) // 2
    cards_left = cards[0:middle]
    cards_right = cards[middle::]
    for card_index in range(len(cards_left)):
        cards_list.append(cards_left[card_index])
        cards_list.append(cards_right[card_index])
    cards = cards_list
print(cards)