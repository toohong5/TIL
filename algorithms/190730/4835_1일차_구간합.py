import sys
sys.stdin = open('input4.txt', 'r')

N = int(input())
for k in range(1, N+1):
    num_cards = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    n = num_cards[0] # 정수의 개수
    m = num_cards[1] # 합할 이웃의 개수

    sum_list = []
    sum = 0
    for i in range(0, n-m+1): # n-m+1 : 마지막 m개가 남아있는 시작위치(규칙찾기)
        for j in range(0, m):
            sum += numbers[i+j] # 0, 1, 2 이런 순으로 더해감.
        sum_list.append(sum) # sum을 리스트에 추가함
        sum=0 # 한 번 끝나면 다시 초기화 시켜야함

    min_sum = sum_list[0]
    max_sum = sum_list[-1]

    for a in sum_list:
        if a < min_sum:
            min_sum = a
        if a > max_sum:
            max_sum = a
    print('#{} {}'.format(k, max_sum - min_sum))