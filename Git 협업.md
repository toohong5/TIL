# Git 협업

## MASTER

- 레퍼지토리 생성
- 폴더 생성

```bash
$ git init
$ git remote add origin '주소'
$ touch test.md # 파일 생성
$ git status
$ git add .
$ git commit -m "first commit"
$ git log
$ git push -u origin master
```

## BRANCH

branch는 기능별로 하는게 좋음(ex> feature/login, feature/signup, ..... )

**같은 파일 같은 라인 수정하면 충돌남....**



fork 누르기

```bash
$ git clone 'fork에서 가져온 주소'
$ git remote -v # origin 2개 있음
$ git remote add upstream `master 주소`
$ git remote -v # 4개 있음
# 중앙(upstream) / fork(origin)
# branch 만들기
# 만들면서 바로 이동.
$ git checkout -b feature/login(이름)
# branch 삭제 = 마스터로 이동해서: $ git branch -d 이름

# 파일 수정 후
$ git status
$ git add .
$ git commit -m ""
$ git push origin 브랜치이름
# github fork 에서 pull request 보내기!!

# master가 merge 한 후 업데이트 하기
$ git checkout master # master 로 이동
$ git pull upstream master # pull 받아옴
```



**master는 건들이지 않는다! (merge만!!)**