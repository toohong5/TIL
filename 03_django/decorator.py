# decorator 함수
# 함수를 매개변수로 받음..
def hello(func):
    def wrapper():
        print('HIHI')
        func()  # bye를 호출
        print('hhhhhhhhhhh')
    return wrapper

@hello # decorator 이름 호출
def bye():
    # 호출되면 인사함
    print('byebye')
bye()

# bye를 건드리지 않고 추가적으로 꾸며준다...