import sys
sys.stdin = open('input2.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    cards = input()
    cards_list = []
    cards_dict = {'S': 13, 'D': 13, 'H': 13, 'C': 13}
    for i in range(0, len(cards), 3):
        cards_list.append(cards[i:i+3])

    c_list = []
    cards_set = set(cards_list)
    if len(cards_set) != len(cards_list):
        print('#{} ERROR'.format(tc))
    else:
        # 첫 글자만 뽑아서 리스트생성
        for card in cards_list:
            c_list.append(card[0])
        # c_list에서 dict의 키값과 같은게 있으면 해당 키의 값 -= 1
        for c in c_list:
            if c in cards_dict.keys():
                cards_dict[c] -= 1
        print('#{} {} {} {} {}'.format(tc, cards_dict['S'], cards_dict['D'], cards_dict['H'], cards_dict['C']))