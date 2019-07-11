# 파일 만들기 1.open() 사용
#변수에 만들고 싶은 파일을 open(파일명, '역할(w,r,a)') 해야 한다.
# open() 할때 r : 읽기 / w : 쓰기(+덮어씌워짐) / a: 추가
f = open('ssafy.txt', 'w')
for i in range(10):
    f.write(f'This is line {i+1}.\n')  # \n : 출력시 엔터
f.close() #끝나고 닫아야함

# 파일 만들기 2.with() 사용
# with 구문(context manager) : close()안쓰기 위해 사용
with open('with_ssafy.txt', 'w') as f:
    for i in range(10):
        f.write(f'This is line {i+1}.\n')
        #자동으로 close() 해줌

# 이스케이프 문자
# \n : 개행문자(다음 줄로 이동)
# \t : 탭문자
# \\ : \출력됨(백슬래쉬 사용하기 위함)
# \' : ' 출력됨
# \" : " 출력됨
# writhelines() : list 를 넣어주면, 요소 하나당 한 줄씩 작성함

with open('ssafy.txt', 'w') as f: # ssafy.txt 에 덮어씀
    f.writelines(['0\n', '1\n', '2\n', '3\n']) # \n써야 다음줄로 이동함

 