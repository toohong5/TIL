```python
# 03_homework.md
# 1
dir(__builtins__)
str()
int()
float()
tuple()
list()

# 2 
3 # 키워드 인자 활용한 뒤 위치인자 사용할 수 없음!!

# 3
None


# 03_workshop.md
string = input()

def palindrome(word):
    word1 = list(word)
    word2 = []
    for i in range(len(word)-1,-1,-1):
        word2.append(word[i])
    
    if word1 == word2:
        return True
    else:
        return False

result = palindrome(string)
print(result)


# 선생님 풀이 ---------------------------------------------------------------------------
#  1.
def is_palindrome(word): # NAAN
    list_word = list(word) # ['N', 'A', 'A', 'N']
    # 리스트 요소의 양쪽 끝끼리 계속 비교하면서 진행
    for i in range(len(list_word)//2): # 2
        if list_word[i] != list_word[-i-1]: # 첫번째는 마지막과 두번째는 마지막에서 두번째와 비교
        	return False
    return True

# 2.Slicing 이용

word == word[::-1] # 스텝이 -1 이므로 역순을 의미함....

```



