import sys
sys.stdin = open('sample_input8.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    words = list(input())

    result = "Exist"

    for i in range(len(words)):
        if words[i] == '*' or words[len(words) - i - 1] == '*':
            break
        elif words[i] != words[len(words) - i - 1]:
            result = "Not exist"
            break

    print('#{} {}'.format(tc, result))
    

    # arr = []

    # i = 0
    # while words[i] != '*':
    #     arr.append(words[i])
    #     words.pop(i)
    #     i += 1

    # if len(words) > len(arr):
    #     k = 0
    #     while len(words) != len(arr):
    #         words.pop(k)
    #         i += 1
    # elif len(words) < len(arr):
    #     j = len(arr) - 1
    #     while len(words) != len(arr):
    #         arr.pop(j)
    
    # if arr == words[::-1]:
    #     result = "Exist"

    #     for j in range(len(words), len(words) - len(arr), -1):
    #         if 
            


    # if words[0] == words[-1] and '*' in words:
    #     result = "Exist"
    # elif words == words[::-1]:
    #     result = "Exist"