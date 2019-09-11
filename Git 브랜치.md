

# Git 브랜치

- 브랜치 : 나뭇가지의 비유적 표현

## 1. 특징

- 매우 가볍다
- 순식간에 브랜치를 만들고 브랜치 사이를 이동 할 수 있다.
- GIT 이 가지고 온 혁신 중 하나는 브랜치 기능을 매우 쓸만한 수준까지 만들었다는 것.



## 2. 브랜치 만들기

```bash
$ git init
$ git branch
$ touch a.txt
$ touch b.txt # 임의의 텍스트 파일 만들기
$ add .
$ git commit -m "first commit"
$ git log
$ git branch # master
$ git branch ssafy
$ git checkout ssafy # ssafy로 돌아감
$ touch c.txt
$ git add .
$ git commit -m "make c.txt"
$ git checkout master
$ git checkout ssafy

```

```bash
$ git checkout -b branch_name (git branch branch_name # 생성 + git check out branch_name)

$ git branch -d feature/test # branch 지우기
$ git log --oneline # master 보여줌
$ git log --oneline --graph # 또 다른법 찾는 중


```

- merge는 master에서!
- merge의 상황

1. faster forward : branch 가 최신버전이 된다.
2. merge-commit
3. merge-conflict

- merge하면서 서로 다른 부모의 자식들이 충돌되

```bash
master


```

```bash
branch

git checkout -b []
git push -u origin feature/test
```

branch에서 작업해서 master로 올려 master에서 합칠지 말지만 결정!!

### 1. feature branch workflow

* Pull request
  * 기능 개발을 끝내고 master에 바로 병합시키는게 아니라, 브랜치를 중앙 원격 저장소에 올리고(push) master에 병합을 요청(merge)
  * 주의사항: 중앙에서 병합을 했다면, 다른 팀원들은 master 브랜치를 pull 받아야 한다.

### 2. forking workflow

중앙 remote(master) - fork-> 원격 remote - clone -> local - upstream -> 중앙 remote

```bash
# branch
# forking 하고 clone하고
# upstream연결..
git remote add upstream [master github 주소(fork뜨기 전 원래 주소)]
git remote -v

# feature/login이라는 브랜치 만들기
git checkout -b feature/login
commit 까지하고
git push -u origin feature/login 에 푸쉬!!

merge master가 승인하고 
git pull upstream master

```





## 상황 1. fast-forward

1. feature/test branch 이동

```bash
$ git checkout -b feature/test
$ (feature/test)
```

2. 작업 완료 후 commit

```bash
touch test.md
git add .
git commit -m "complete test.md"
```

3. master 이동

```bash
git checkout master
$ (master)
```

4. master에 병합

```bash
$ git merge feature/test
```

5. 결과
   - 단순히 HEAD가 최신 COMMIT으로 이동
   - feature/test branch 생성 이후 master branch의 이력에 변화가 없었기 때문
6. branch  삭제

```bash
$ git branch -d feature/test
```

<hr>

## 2. merge commit(3)

1. feature/login branch로 이동

```bash
$ git checkout -b feature/login
```

2. 작업 완료 후 commit

```bash
$ touch login.md
$ git add .
$ git commit -m "complete login.md"
```

3. master로 이동

```bash
$ git checkout master
```

4. master에 추가 commit 생성

```bash
$ touch master.md
$ git add .
$ git commit -m "fix master.md"
```

5. master에 병합

```bash
$ git merge feature/login
```

6. 자동으로 merge commit 발생

```bash
Merge brach 'feature/login'

# please enter a commit ...
```

- Vim 에디터로 열림
- 메세지를 수정하고자하면 i로 편집모드를 바꾼 다음에 commit을 수정하고 
- `esc` + `:wq`   를 통해 저장 및 종료

7.  commit 그래프 확인하기

```bash
$ git log --oneline --graph

* 8d7a4f2 (HEAD -> master)  fix a.txt in master
*   2c1937f (feature/article) Merge branch 'feature/signout'
|\
| * 47a0a67 Complete login.txt
| * fc4458d Complete sighout.txt
* | 195d1d9 Make master.txt
|/
* 64356e5 complete test.txt
* 005bef3 first commit

```

8. branch 삭제



### 3. merge conflict

1. feature/article branch 생성 및 이동

   ```bash
   $ git checkout -b feature/article
   ```

2. 작업 완료 후 commit

   ```bash
   # 충돌을 만들어낼 파일에 코드를 작성
   $ git add .
   $ git commit -m "ficed"
   ```

3. master로 이동

   ```bash
   $ git checkout master
   ```

4. master에 추가 commit 만들기

   ```bash
   # feature/article branch 에서 수정한 파일과 동일 파일의 같은 위치를 수정
   $ git add .
   $ git commit -m "fixed master update"
   ```

```
5. master 에 병합

   ```bash
   $ git merge feature/article
   ```

6. merge confict 발생

   ```bash
   $ git merge feature/article
   Auto-merging a.txt
   CONFLICT ...
   Automatic merge faild; fix conflicts and then commit result.
   ```

7. 충돌 확인 및 해결

   ```bash
   # 충돌이 일어난 파일 열기
   # 그럼 아래와 같은 내용이 있다.
   
   <<<<<<<< HEAD
   master 에서 작성한 내용
   ========
   feature/article 에서 작성한 내용
   >>>>>>>> feature/article
   
   # 원하는 코드로 수정
   ```

8. merge commit 진행

   ```bash
   $ git add .
   $ git commit
   ```

   - commit 메세지는 미리 작성되어 있음

9. commit 그래프 확인

   ```bash
   $ git log --oneline --graph
   *   7238aa2 (HEAD -> master) Merge branch 'feature/article'
   |\
   | * 8e84920 (feature/article) fix a.txt
   * | 28faf63 fix a.txt in master
   |/
   *   2743900 Merge branch 'feature/login'
   |\
   | * 29a92c0 Complete login.txt
   | * 38e2723 Complete signout.txt
   * | 278eaf5 Make master.txt
   |/
   * a52a916 complete test.txt
   * 8988463 first commit
   ```

10. branch 삭제

    ```bash
    $ git branch -d feature/article
    ```
```

rebase reset stash 는 심화git개념