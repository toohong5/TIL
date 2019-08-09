import sys
sys.stdin = open('input2_4.txt', 'r')

N = int(input())

for i in range(1, N + 1):
    n = int(input())
    num = list(map(int, input().split()))
    result = []

    for j in range(5):
        result.append(str(max(num)))
        num.remove(max(num))
        result.append(str(min(num)))
        num.remove(min(num))

    print('#{} {}'.format(i, ' '.join(result)))