import sys
sys.stdin = open('input2_4.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = []
    # i = 0
    # for i in range(0, N - 1, 2):
    #     if len(arr) != 0:
    #         result[i] = max(arr)
    #         result[i+1] = min(arr)
    #         arr.pop(arr.index(max(arr)))
    #         arr.pop(arr.index(min(arr)))
    #     elif len(arr) == 0:
    #         break
    # print('# {} {}'.format(tc, ' '.join(result)))

    for _ in range(5):
        result.append(str(max(arr)))
        arr.remove(max(arr))
        result.append(str(min(arr)))
        arr.remove(min(arr))
    
    print('#{} {}'.format(tc, ' '.join(result)))
