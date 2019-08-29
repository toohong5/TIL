import sys
sys.stdin = open('sample_input5.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    arr = list(input())
    S = []
    num = 0
    for i in arr:
        if i.isdecimal():
            num = i
        elif i in '+*':
            if i == '+' and 