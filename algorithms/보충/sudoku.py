import sys
sys.stdin = open('sudoku_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    sudoku = []
    # nums = [i for i in range(1, 10)]
    for i in range(9):
        s = list(map(int, input().split()))
        sudoku.append(s)
    
    # 행, 열 3*3에서 겹치는 숫자가 없어야 한다!
    result = 0
    for r in range(9):
        set_s = set(sudoku[r])
        if len(set_s) != len(sudoku[r]):
            result += 0
            # break
        else:
            result += 1
        c_list = []
        for c in range(9):
            c_list.append(sudoku[c][r])
        set_c = set(c_list)
        if len(set_c) != len(c_list):
            result += 0
            # break
        else:
            result += 1
   
    # 3*3 행렬들
    # result2 = 0
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            t_list = []
            for r in range(x, x + 3):
                for c in range(y, y + 3):
                    t_list.append(sudoku[r][c])
            t_set = set(t_list)
            if len(t_set) != len(t_list):
                result += 0
                # print('#{} {}'.format(tc, result2))
                # break
            else:
                result += 1
        # if result2 == 0:
        #     break
    # if result2 == 1:
    #     print('#{} {}'.format(tc, result2))

    if result == 27:
        r = 1
    else:
        r = 0
    print('#{} {}'.format(tc, r))