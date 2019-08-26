import sys
sys.stdin = open('sample_input7.txt', 'r')

n = int(input())
for tc in range(1, n + 1):
    word = list(input())
    
    result = "Not exist"
    for i in range(len(word)):
        if word[i] == '?':
            word[i] = word[len(word) - i -1]
    
    if word == word[::-1]:
        result = "Exist"

    print('#{} {}'.format(tc, result))
    
    