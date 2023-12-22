with open("Day 07/data.txt","r") as file:
    data = file.read().split("\n")
# print(data)

hands = {"5kind": [], "4kind": [], "fh": [], "3kind": [], "2p": [], "1p":[], "hc": []}
ranks = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]

for line in data:
    hand, bet = line.split(" ")
    hand = hand.replace("T","a")
    hand = hand.replace("J","0")
    hand = hand.replace("Q","c")
    hand = hand.replace("K","d")
    hand = hand.replace("A","e")
    # print(hand, bet)
    cards = {}
    for card in hand:
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    # print(cards)
    # max_count = 0
    # print(sorted(cards.items(), reverse=True, key=lambda x: x[0]))
    # for value, count in sorted(cards.items(), reverse=True, key=lambda x: x[0]):
    #     if count > max_count and value != "f":
    #         to_replace = value
    #         max_count = count
    joker_count = cards.pop("0",0)
    if not cards:
        hands["5kind"].append((hand, bet))
    elif max(cards.values()) + joker_count == 5:
        hands["5kind"].append((hand, bet))
    elif max(cards.values()) + joker_count == 4:
        hands["4kind"].append((hand, bet))
    elif max(cards.values()) + joker_count == 3 and min(cards.values()) == 2:
        hands["fh"].append((hand, bet))
    elif max(cards.values()) + joker_count == 3:
        hands["3kind"].append((hand, bet))
    elif max(cards.values()) + joker_count == 2 and len(cards) == 3:
        hands["2p"].append((hand, bet))
    elif max(cards.values()) + joker_count == 2:
        hands["1p"].append((hand, bet))
    else:
        hands["hc"].append((hand, bet))
# print(hands)

total = 0
winning_rank = len(data)
for hand_type in hands:
    hand_list = sorted(hands[hand_type],reverse=True, key=lambda x: x[0])
    # print(hand_list)
    for hand, bet in hand_list:
        # print(bet, winning_rank)
        total += int(bet) * winning_rank
        winning_rank -= 1

print(total)