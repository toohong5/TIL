# 월말평가 풀이

# 1 나누어 떨어지는 숫자들
def can_divide(numbers, divisor):
    # 1. 일반적인 풀이
    result = []

    for number in numbers:
        if number % divisor == 0:
            result.append(number)
    if result == []:
        result.append(-1)

    return sorted(result)

    # 2. list comprehension
    result = [number for number in numbers if not number % divisor]
    result = sorted(result) if result else [-1] # 있으면 sorted, 없으면 -1 할당
    return result
# 2 알파벳 카운트
def alphabet_count(word):
    # 1. 일반적인 풀이
    result = {}
    for char in word:
        # result에 있으면 +1, 처음이면 1
        if result.get(char):
            result[char] += 1
        else:
            result[char] = 1
    return result

    # 2. 딕셔너리 컴프리헨션
    return {char: word.count(char) for char in word}
# 3 문자열 요약하기
# 반복되는 문자열에서 동일한 문자가 등장해도 연속되지 않으면 다시 count 해야한다.
def summary(word):

    result = []
    tmp_list = [] # 잠시 거쳐가는 곳

    # 1-1 단어에서 문자를 하나씩 꺼낸다.
    for char in word:
        # 1-2 tmp_list가 빈 리스트가 아니고 + temp_list의 마지막 값과 char가 같지 않으면 
        # 마지막 요소가 char와 같지 않다는 것은(True) 동일한 문자가 아닌 다른 문자의 시작이라는
        # 임시리스트의 마지막 요소를 결과 리스트에 추가하고 그 길이도 추가한다.
        if tmp_list and tmp_list[-1] != char:
            # 1-3 임시 리스트에 마지막 값을 추가
            result.append(tmp_list[-1])
            # 1-4 임시 리스트에 길이를 추가
            result.append(f'{len(tmp_list)}')
            # 1-5 임시 리스트를 비워준다.
            tmp.list.clear()
        # 1-6 새로운 글자를 계속 tmp_list에 넣는다
        # for 문 안에 있으니 for문이 끝날 때 까지 반복한다.
        tmp_list.append(char)
    # 1-7 임시리스트의 마지막 값과 그 길이를 넣어준다.
    # 마지막 요소는 for문이 다 끝나 버리니 tmp_list[-1] != char 조건에서 비교할 char가 없기 때문에 if문이 아예 동작하지 않게 된다.
    # 그래서 마지막으로 append를 해줘야 한다.
    result.append(tmp_list[-1])
    result.append(f'{len(tmp_list)}')
    # result = ['a', '2', 'b', '2', 'a', '2', 'c', '2']
    return ''.join(result)

# 4 나만의 단어장
class Word:
    def __init__(self):
        self.wordbook = {}
    def add(self, eng, kor):
        self.eng = eng
        self.kor = kor
        self.wordbook[eng] = kor

    def delete(self, eng):
        if eng in self.wordbook:
            self.wordbook.pop(eng)
            return True 
        else:
            return False
    def print(self):
        for eng, kor in self.wordbook.items():
            print(f'{eng}: {kor}')

    
# 5 도형만들기
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def get_area(self):
        return abs(self.p1.x - self.p2.x) * abs(self.p1.y - self.p2.y)

    def get_perimeter(self):
        return abs(self.p1.x - self.p2.x) * 2 + abs(self.p1.y - self.p2.y) * 2

    def is_square(self):
        return abs(self.p1.x - self.p2.x) == abs(self.p1.y - self.p2.y):
