import sys
sys.stdin = open('input3.txt', 'r')

N = int(input())
for k in range(1, N+1):
    num_cards = int(input())
    cards = input()

    cards_count = [0] * 10

    for i in range(0, num_cards):
        if cards[i] not in cards_count:
            cards_count[int(cards[i])] += 1
        elif cards[i] in cards_count:
            cards_count[int(cards[i])] += 1

    max_num = cards_count[0]
    num = 0
    for j in range(1, len(cards_count)):
        if max_num <= cards_count[j]:
            max_num = cards_count[j]
            num = j
    print('#{} {} {}'.format(k, num, max_num))