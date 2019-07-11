# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')
total_score = 0
for subject_score in score.values():
    total_score = total_score + subject_score
    #total_score += subject_score
avg_score = total_score / len(score)
print(avg_score)


# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
total_score1 = 0
total_score2 = 0
scores_a = scores.get('a').values()
scores_b = scores.get('b').values()

for score in scores_a:
    total_score1 += score
for score in scores_b:
    total_score2 += score

avg_a = 0
avg_a = total_score1 / len(scores_a)

avg_b = 0
avg_b = total_score2 / len(scores_b)

print(f'a의 평균은 {avg_a}')
print(f'b의 평균은 {avg_b}')

avg_total = 0
avg_total = (avg_a + avg_b) / 2
print(f'전체 평균은 {avg_total}입니다.')

"""
선생님 풀이 1)
value안의 value가져오기!

total_score = 0
count = 0 #for문이 도는 횟수

for person_score in scores.values():
    for individual_score in person_score.values():
        total_score += individual_score
        count += 1

avg_score = total_score / count
print(avg_score)

2)
avg_score = list(map(lambda d: sum(d.values()) / len(d), scores.values()))
result = sum(avg_score) / len(avg_score)
print(result)
"""



# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""

# items()가 필요한 경우임

for name, temp in city.items():
    # 1회차 : name= 서울, temp = [-6,-10,5]
    avg_temp = sum(temp)/len(temp) # 리스트의 합/길이
    print(f'{name} : {avg_temp:.1f}')


# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')

count=0
for name, temp in city.items():
    # 첫 번째 시행 때
    # name = '서울'
    # temp = '[-6, -10, 5]
    # 단 한번만 실행되는 조건이 필요

    if count == 0: # 첫 기준점 설정
        hot_temp = max(temp) #서울 온도 중 가장 높은값 저장됨
        cold_temp = min(temp) #서울 온도 중 가장 낮은 값 저장됨
        hot_city = name
        cold_city = name
    else:
        # 최저 온도가 cold_temp 보다 낮으면, cold_temp에 값을 넣고,
        if min(temp) < cold_temp:
            cold_temp = min(temp) #낮은값을 넣는다
            cold_city = name # 낮은 지역 이름 넣음
        if max(temp) > hot_temp:
            hot_temp = max(temp) # 더 높은 값 저장
            hot_city = name
        # 최고 온도가 hot_temp 보다 높으면, hot_temp에 값을 새로 넣는다.

    count += 1
print(f'최고로 더웠던 지역은 {hot_city}, 최고로 추웠던 지역은 {cold_city}')



# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?
# (=서울 온도 리스트에 2가 있나요??와 같은 말임)
# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
if 2 in city['서울']:
    print('네 있어요')
else:
    print('아니요 없어요')