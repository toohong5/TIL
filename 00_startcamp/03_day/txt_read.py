# read() : 개행문자를 포함한 하나의 문자열

with open('with_ssafy.txt', 'r') as f:
    all_text = f.read()
    print(all_text)

# readlines() : 파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 list로 만들어냄
with open('with_ssafy.txt', 'r') as f:
    lines = f.readlines() #리스트가 담길 변수, for문으로 출력할 예정
    for line in lines:
        print(line.strip()) #'문자열'.strip() : 개행문자 지워줌!
        # print(dir(line)) # dir(변수) : 해당 변수 뒤에 어떤 것들을 사용할 수 있는지 알려주는 함수