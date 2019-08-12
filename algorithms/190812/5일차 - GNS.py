import sys
sys.stdin = open('GNS_test_input.txt', 'r')

N = int(input())
for i in range(N):
    arr = list(map(str, input().split()))
    case_num = arr[0]
    len_list = int(arr[1])

    num_list = list(input().split())

    nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    new=[]
    for num in nums:
        new.append((num + ' ') * num_list.count(num))
    
    print('{}'.format(case_num))
    for n in new:
        print('{}'.format(n))
    print()
    

    # for num in num_list:
    #     for n in nums:
    #         if num == n:

    # for k in num_list:
    #     for p in nums:
    #         if p[0] == k:
    #             num_list[0] = k
                
    # for k in num_list:
    #     if k == 'ZRO':
    #         dict_nums[0] = k
    #     elif k == 'ONE':
    #         dict_nums[1] = k
    #     elif k == 'TWO':
    #         dict_nums[2] = k
    #     elif k == 'THR':
    #         dict_nums[3] = k
    #     elif k == 'FOR':
    #         dict_nums[4] = k
    #     elif k == 'FIV':
    #         dict_nums[5] = k
    #     elif k == 'SIX':
    #         dict_nums[6] = k
    #     elif k == 'SVN':
    #         dict_nums[7] = k
    #     elif k == 'EGT':
    #         dict_nums[8] = k
    #     elif k == 'NIN':
    #         dict_nums[9] = k

    # for n in num_list:
    #     for key, val in dict_nums.items():
    #         if 
    # for j in num_list:
    #     if j == 'ZRO':
    #         num_list[0] = j
        