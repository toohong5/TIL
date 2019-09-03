class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

def addtoLast(data):    # 마지막에 데이터 삽입
    global Head
    if Head == None:    # 빈 리스트이면
        Head = Node(data, None)
    else:
        p = Head
        while p.link != None:   # 마지막 노드 찾을때까지
            p = p.link
        p.link = Node(data, None)

def delete(pre):
    if pre == None or pre.link == None:
        print('error')
    else:
        pre.link = pre.link.link

def deleteFirst():
    global Head
    if pre == None:
        print('error')
    else:
        Head = Head.link

def addtoFirst(data):
    global Head
    Head = Node(data, Head)

def add(pre, data):
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)

import sys
sys.stdin = open('sample_input2.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    Head = None
    N, M = map(int, input().split())
    arr1 = list(map(int, input().split()))

    for i in range(len(arr1)):
        addtoLast(arr1[i])
    
    for _ in range(M - 1):
        arr2 = list(map(int, input().split()))
        p = Head
        if p.data <= arr2[0]:
            while p.link != None:
                if p.link.data <= arr2[0]:
                    p = p.link
                elif p.link.data > arr2[0]:
                    break
            for k in range(-1, -len(arr2)-1, -1):
                add(p, arr2[k])
        else:
            for k in range(-1, -len(arr2)-1, -1):
                addtoFirst(arr2[k])

    result = []
    while Head.link != None:
        result.append(Head.data)
        Head = Head.link
    result.append(Head.data)

    print('#{}'.format(tc), end = ' ')
    for data in range(-1, -10, -1):
        print(result[data], end = ' ')
    print(result[-10])