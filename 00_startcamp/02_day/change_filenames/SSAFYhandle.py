import os

# 1. 해당 파일들이 있는 위치로 이동. chdir()사용
os.chdir(r'C:\Users\student\Desktop\TIL\00_startcamp\02_day\change_filenames') # r 은 윈도우 환경에서 \의 이스케이프 문자 역할이 아닌 문자열 자체로 인식하기 위해 사용!

# 2. 현재 폴더 안에 모든 파일 이름을 수집. listdir() 사용
filenames = os.listdir('.') #''안에 디렉토리 주소입력, . 은 현재위치를 뜻함

# 3. 각각의 파일명을 돌면서 수정한다. rename(이전파일명, 바꿀파일명)사용
# for filename in filenames:
#     os.rename(filename, f'SAMSUNG_{filename}')

# 4. SAMSUNG을 SSAFY로 변환. rename(이전이름, 바꿀이름), replace('바꿀문자열', '바꾸고 싶은 문자열')
for filename in filenames:
    os.rename(filename, filename.replace('SAMSUNG_SAMSUNG_SAMSUNG_', 'SSAFY'))