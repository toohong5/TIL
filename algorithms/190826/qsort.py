def qsort(a, low, high):
    if low < high:
        pivot = partition(a, low, high) # 맨왼쪽은 low, 맨 오른쪽은 high으로 설정
        qsort(a, low, pivot - 1)
        qsort(a, pivot + 1, high)

def partition(a, pivot, high): # 피벗 구하기 => 왼쪽(low)를 피벗으로 정함
    i = pivot + 1 # 피벗 다음 값
    j = high # j를 감소시켜감..
    while True:
        while i < high and a[i] < a[pivot]: # 피벗보다 큰값 찾기
            i += 1
        while j > pivot and a[j] > a[pivot]: # 피벗보다 작은 값 찾기
            j -= 1
        if j <= i:
            break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    a[pivot], a[j] = a[j], a[pivot]
    return j

a = [54, 88, 77, 26, 93, 17, 49]
print('정렬 전: \t', a)
qsort(a, 0, len(a)-1)
print('정렬 후: \t', a)

# 왼쪽에는 피벗보다 작은값들 오른쪽에는 피벗보다 큰값들이 모인다 => 분할
# 왼쪽 부분 리스트에 대해 다시 퀵정렬, 오른쪽 부분 리스트에 대해 다시 퀵정렬 => 반복...
