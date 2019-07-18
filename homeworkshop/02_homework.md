```python
# 02_homework.md

# 1.
mutable = list, set, dictionary # value값만..key값은 불변
immutable = string, tuple, range

# 2.
list = list(range(1,51))
print(list[0::2]) # slicing => [시작:끝:단위]

#3.
classmates = {'조규홍': 29, '이병주': 27, '박홍은': 24}

 
# 02_workshop.md

# 1.
n, m = 5, 9

for i in range(m): #전체적으로 m번 돈다
	print("*" * n)
"""
for i in range(m):
	for j in range(n):
		print('*', end='')
	print()
"""

# 2.
# value값들을 더해준다.
student = {'python': 80, 'algorithm': 99, 'django': 89, 'flask': 83}
sum=0
for score in student.values():
    sum=sum+score
"""
avg = sum(student.values())/len(student.keys()) 도 가능함!
"""

print(f'평균은 {sum/len(student)} 입니다.')

# 3. 
blood_types = ['A', 'B', 'A', 'O','AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

type_blood = {}

for type in blood_types:
    type_blood[type] = blood_types.count(type)

print(type_blood)

"""
for blood in blood_types:
	if type_blood.get(blood):
		type_blood[blood] += 1
	else:
		type_blood[blood] = 1
print(type_blood)
"""
```

