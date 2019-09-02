import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bus = [0] * 5001
    for i in range(N):
        a, b = map(int, input().split())
        for j in range(a, b+1):
            bus[j] += 1
    
    P = int(input())
    print('#{}'.format(tc), end=' ')
    for _ in range(P-1):
        print(bus[int(input())], end=' ')
    print(bus[int(input())])