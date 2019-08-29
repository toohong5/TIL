def tm(start, end):
    if start == end:
        return start
    a = tm(start, (start + end) // 2)
    b = tm((start + end) // 2 + 1, end)
    return rsp(a, b)
        
def rsp(a, b):
    if (arr[a - 1] == 1 and arr[b - 1] == 3) or (arr[a - 1] == 2 and arr[b - 1] == 1) or (arr[a - 1] == 3 and arr[b - 1] == 2) or (arr[a - 1] == arr[b - 1]):
        return a
    else:
        return b
   
import sys
sys.stdin = open('sample_input3.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 1: 가위 / 2: 바위 / 3: 보
    # index값
    start = 1
    end = N

    print('#{} {}'.format(tc, tm(start, end)))

# -------------------------------------------------------------

