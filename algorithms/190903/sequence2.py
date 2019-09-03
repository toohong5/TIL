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

N = int(input())

for i in range(1, N+1):
    Head = None
    length, nums = map(int, input().split())
    first_list = list(map(int, input().split()))
    for k in range(length):
        addtoLast(first_list[k])

    for j in range(nums-1):
        next_list = list(map(int, input().split()))
        p = Head
        if p.data <= next_list[0]:
            while p.link != None:
                if p.link.data <= next_list[0]:
                    p = p.link
                elif p.link.data > next_list[0]:
                    break
            for k in range(-1, -len(next_list)-1, -1):
                add(p, next_list[k])
        else:
            for k in range(-1, -len(next_list)-1, -1):
                addtoFirst(next_list[k])

    result = []
    while Head.link != None:
        result.append(Head.data)
        Head = Head.link
    result.append(Head.data)

    print('# {}'.format(i), end=' ')
    for v in range(-1, -10, -1):
        print(result[v], end=' ')
    print(result[-10])