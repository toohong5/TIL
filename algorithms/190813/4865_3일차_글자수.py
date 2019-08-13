import sys
sys.stdin = open('sample_input3.txt', 'r')

N = int(input())
for i in range(1, N + 1):
    str1 = list(input())
    str2 = list(input())
    count = 0
    count_list = []
    for word in str1:
        for w in str2:
            if word == w:
                count += 1
        count_list.append(count)
        count = 0
    print('#{} {}'.format(i, max(count_list)))
