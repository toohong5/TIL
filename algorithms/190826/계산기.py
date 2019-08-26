c = '2+3*4/5'
S = []
for i in c:
    if i not in '+-*/':
        print(i, end='')
    else:
        S.append(i)
for j in range(len(S)):
    print(S.pop(), end='')