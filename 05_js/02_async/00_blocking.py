from time import sleep

# 3초간 자는 함수
def sleep_3s():
    sleep(3)
    print('Wake up!')

print('Start sleeping')
sleep_3s() # 얘가 종료 될 때 까지 뒤에는 동작하지 않음...(코드의 실행을 블로킹함.)
print('End of program')