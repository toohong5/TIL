import sys
sys.stdin = open('sample_input6.txt', 'r')

n = int(input())
for i in range(1, n+1):
    m = int(input())
    total = ''
    for tc in range(m):
        char, num = input().split()
        num = int(num)
        words = char * num
        total += words
    print('#{}'.format(i))
    for i in range(len(total)):
        if (i+1) % 10 != 0:
            print(total[i], end='')
        else:
            print(total[i], end='\n')
    print()
    

