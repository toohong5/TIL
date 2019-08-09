import sys
sys.stdin = open('input2_2.txt', 'r')

N = int(input())
A = list(range(1, 13))

result = []
for i in range(1 << len(A)):
    a = []
    for j in range(len(A) + 1):
        if i & (1 << j):
            a.append(A[j])
    result.append(a)

for m in range(1, N + 1):
    nk = list(map(int, input().split()))
    n = nk[0]
    k = nk[1]
    count = 0
    for r in result:
        if len(r) == n and sum(r) == k:
            count += 1
    print('#{} {}'.format(m, count))

