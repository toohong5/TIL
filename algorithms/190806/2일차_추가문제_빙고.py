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

<<<<<<< HEAD
answer = []
for p in range(len(answer_list)):
    for q in range(len(answer_list[0])):
        answer.append(answer_list[p][q])

N = len(bingo_list)
M = len(bingo_list[0])

count = 0
result = 0
for i in range(len(answer)):
    for p in range(N):
        for q in range(M):
            if str(answer[i]) == str(bingo_list[p][q]):
                bingo_list[p][q] = 0

        if bingo_list[p] == 0:
            count += 1
    if count == 3:
        result = i+1
        break

print(result)





# # 

# for p in range(N):
#     for q in range(M):
#         if str(answer_list[p][q]) in bingo_list:
#             bingo_list[p][q] = 0
#             print(answer_list[p][q])
# print(bingo_list)
=======
N = len(bingo_list)
M = len(bingo_list[0])

# 행, 열, 대각의 합이 0이면 count+1

for p in range(N):
    for q in range(M):
        if str(answer_list[p][q]) in bingo_list:
            bingo_list[p][q] = 0
            # print(answer_list[p][q])
print(bingo_list)
>>>>>>> bf6954ae6deca47970c3b529deca56792dfe04d4
