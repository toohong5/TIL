# 노드
class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

def push(i):            # 원소 i를 스택 top(맨앞) 위치에 push
    global top
    top = Node(i, top)  # 새로운 노드 생성

def pop():              # 스택의 top을 pop
    global top
    if top == None:     # 빈리스트 이면
        print('error')
    else:
        data = top.data
        top = top.link  # top이 가리키는 노드를 바꿈
        return data

top = None
push(3)
push(4)
push(5)
push(6)
pop()

while top.link != None:
    print(top.data, end='->')
    top = top.link
print(top.data)