import sys
sys.stdin = open('sample_input1.txt', 'r')

N = int(input())
for tc in range(1, N + 1):
    p = input()
    t = input()

    n, m = len(t), len(p)
    result = 0
    for s in range(n - m + 1):
        j=0
        while j < m:
            if p[j] != t[s + j]
                result = 0
                break
            j += 1
        if j == m:
            result = 1
            break
