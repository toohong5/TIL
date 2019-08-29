# from queue import Queue

# Q = []
# front = rear = -1
# def enQueue(i):
#     global rear
#     if isFull() : print("Queue_Full")
#     else:
#         rear += 1
#         Q[rear] = i

# def isFull():
#     global rear
#     return rear == len(Q) - 1

# def deQueue():
#     global front
#     if isEmpty():
#         print("Queue_Empty")
#     else:
#         front += 1
#         return Q[front]

# def isEmpty():
#     return front == rear

# enQueue(1)
# enQueue(2)
# enQueue(3)
# print(Q)
# print(deQueue())
# print(deQueue())
# print(deQueue())

# --------------------------------------------------------
# 모듈 이용한 방법
# import queue 
# from queue import Queue
# q = Queue()       # 빈 큐 생성
# q.put('1')
# q.put('2')
# q.put('3')

# while not q.empty():   # 빌때까지 꺼낸다
#     print(q.get())

#------------------------------------------
# 원형 큐 구현

def isEmpty():
    return front == rear

def isFull():
    return (rear+1) % len(cQ) == front

def enQueue(item):
    global rear
    if isFull():
        print("Queue_Full")
    else:
        rear += 1 % len(cQ)
        cQ[rear] = item

def deQueue():
    global front
    if isEmpty():
        print("Queue_Empty")
    else:
        front += 1 % len(cQ)
        return cQ[front]


cQ_size = 3
cQ = [0] * cQ_size

front = rear = 0

enQueue('A')
enQueue('B')
enQueue('C')
print(deQueue())
print(deQueue())
print(deQueue())

"""
Queue_Full => a, b 넣은 후 꽉 찬상태로 시작
A -> a 삭제
B -> b 삭제
Queue_Empty -> 빈상태
None -> 아무것도 없음..
"""