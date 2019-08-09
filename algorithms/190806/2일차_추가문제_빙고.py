import sys
sys.stdin = open('input2_6.txt', 'r')

bingo_list = []
answer_list = []
for i in range(5):
    bingo = list(map(int, input().split()))
    bingo_list.append(bingo)

for j in range(5,10):
    answer = list(map(int, input().split()))
    answer_list.append(answer)

N = len(bingo_list)
M = len(bingo_list[0])

# 

for p in range(N):
    for q in range(M):
        if str(answer_list[p][q]) in bingo_list:
            bingo_list[p][q] = 0
            print(answer_list[p][q])
print(bingo_list)
