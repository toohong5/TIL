import sys
sys.stdin = open('sample_input1.txt', 'r')

N = int(input())
for i in range(1, N + 1):
    str1 = input()
    str2 = input()
    
    n, m = len(str2), len(str1)

    p = q = 0
    result = 0
    for k in range(n-m+1):
        j = 0
        while j < m:
            if str1[j] != str2[k + j]:
                result = 0
                break
            j += 1
        if j == m:
            result = 1
            break
    print('#{} {}'.format(i, result))
    
    # if str1 in str2:
    #     print('#{} 1'.format(i))
    # else:
    #     print('#{} 0'.format(i))
    
   
