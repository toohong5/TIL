import sys
sys.stdin = open('input3.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    words = input()
    arr = [0] * 10
    
    for i in range(n):
        arr[int(words[i])] += 1
    
    max = 0
    index = 0
    for w in range(len(arr)):
        if arr[w] >= max:
            max = arr[w]
            index = w
        
    print(index, max)
