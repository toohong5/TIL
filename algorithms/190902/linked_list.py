# 노드
class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link
# 노드 삽입    
def addtoFirst(data):           # 첫 노드에 데이터 삽입
    global Head
    Head = Node(data, Head)     # 새로운 노드 생성
 # 새로 만들어질 노드는 그 전 노드를 가리키게 된다.

# 중간에 삽입
def add(pre, data):
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)

# 마지막에 데이터 삽입
def addtoLast(data):
    global Head
    if Head == None: # 빈리스트 이면
        Head = Node(data, None)     # 새로만든 노드의 link에 None
    else:
        p = Head
        while p.link != None:       # 마지막 노드 찾을때 까지
            p = p.link
        p.link = Node(data, None)   # p의 링크가 새로 만든 노드를 가리키게 한다.

# pre 다음 노드 삭제
def delete(pre):
    if pre == None or pre.link == None:
        print('error')
    else:
        pre.link = pre.link.link

# 처음 노드 삭제
def deleteFirst():
    global Head
    if pre == None:
        print('error')
    else:
        Head = Head.link

data = [1, 2, 3, 4]
Head = None

# for i in range(len(data)):
#     addtoLast(data[i])

for i in range(len(data)):
    addtoFirst(data[i])
# # Head가 4를 가리키고 있음..4의 link는 3의 주소값 갖고 있음!
# add(Head, 8)

# head(pre)는 4노드를 가리킴...
delete(Head)

while Head.link != None:
    print(Head.data, end = '->')
    Head = Head.link
# None인 경우 출력(맨 마지막 노드 출력)
print(Head.data)