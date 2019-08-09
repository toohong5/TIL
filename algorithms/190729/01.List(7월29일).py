import sys
sys.stdin = open('input.txt', 'r')

for k in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))

    sum = 0

    for i in range(2, len(buildings)-2):
        if buildings[i] > buildings[i+1] and buildings[i] >buildings[i+2] and buildings[i] > buildings[i-1] and buildings[i] > buildings[i-2]:
        # buildings[i] > (buildings[i-2] and buildings[i-1] and buildings[i+1] and buildings[i+2])
            max = 0
            for j in range(5):
                if j==0:
                    max = buildings[i-2]
                elif max < buildings[i-2+j] and j != 2:
                    max = buildings[i-2+j]
            sum += buildings[i] - max
    print('#{} {}'.format(k, sum))

    if max < buildings[i]:
