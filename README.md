# Do it! 자료구조 알고리즘 하계 스터디 (2026 여름)

원본: easysIT/doit_dsalgo_with_python

## 📌 Notion
https://app.notion.com/p/Doit-3914098e869c8046b76ccbb021ba58d0

## 📁 폴더 구조

- chapXX/answer/   : 원본 정답 코드 (참조용, 수정 금지)
- chapXX/{이름}/    : 각자 실습 코드 (본인 것만 수정)

## 🚀 시작하기 — Repo 가져오기

### 0. 사전 조건
- Collaborator 초대 수락 완료 (이메일/GitHub 알림에서 Accept)
- Git 설치 확인: 터미널에 `git --version` 쳐서 버전 나오면 OK

### 1. Repo URL 복사
GitHub repo 페이지 → 초록색 `<> Code` 버튼 → HTTPS 탭 → URL 복사

### 2. 원하는 위치에 clone
```bash
cd ~/study
git clone https://github.com/rhslxkd/doit_dsalgo_with_python.git
```

### 3. 폴더 이동 및 확인
```bash
cd doit_dsalgo_with_python
ls                    # chap01~09, README.md 보이면 성공
```

### 4. Git 계정 정보 설정 (처음 git 쓰는 경우 필수)
```bash
git config --global user.name "본인이름"
git config --global user.email "GitHub 가입 이메일"
```

### 5. 본인 폴더 확인
```bash
ls chap01             # answer, hyeonsoo, hyeonjin, bumkwan, younghyeon, eunseong 다 보이면 정상
```

### 6. VS Code로 열기
```bash
code .
```
`code` 명령이 안 먹으면: VS Code에서 `⌘⇧P` → "Shell Command: Install 'code' command in PATH" 실행 → 터미널 재시작.

## 🐍 환경 설정 (Python + conda)

이 프로젝트는 `doit`이라는 이름의 conda 가상환경(Python 3.11)에서 작업합니다.
컴퓨터 상태에 따라 아래 두 가지 경로 중 하나를 따라가세요.

---

### A. conda가 이미 설치되어 있는 경우

터미널에 아래 입력해서 확인:
```bash
conda --version
```
버전이 나오면 이 경로로 진행:

```bash
conda create -n doit python=3.11 -y
conda activate doit
```

확인:
```bash
python --version     # Python 3.11.x
which python          # .../envs/doit/bin/python 경로면 정상
```

---

### B. conda가 없는 경우 (Mac 기준)

#### 1. Homebrew 확인 및 설치
```bash
brew --version
```
없으면:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### 2. miniforge(conda) 설치
```bash
brew install miniforge
```

#### 3. conda 초기화
```bash
conda init zsh
```
**⚠️ 중요: 이 명령 실행 후 터미널을 완전히 종료하고 새로 열어야 적용됩니다.**
같은 창에서 계속하면 `conda: command not found`가 뜹니다.

#### 4. 새 터미널에서 확인
```bash
conda --version
```
버전이 나오면 → 위 **A 항목**으로 이동해서 `doit` 환경 생성.

---

### VS Code에서 인터프리터 연결

1. `⌘⇧P` → `Python: Select Interpreter`
2. 목록에서 `Python 3.11.x ('doit': conda)` 선택
3. 목록에 안 보이면 "Enter interpreter path" → 직접 입력:

### C. Windows 사용자

#### 1. conda 있는지 확인
PowerShell(관리자 아님, 일반)에서:
```powershell
conda --version
```
버전 나오면 → 아래 "환경 생성"으로 바로 이동.

#### 2. conda 없으면 — Miniforge 설치
1. https://github.com/conda-forge/miniforge#miniforge3 접속
2. **Miniforge3 Windows x86_64** 설치파일 다운로드
3. 설치 시 **"Add Miniforge3 to my PATH environment variable"** 체크 (기본은 비추천으로 되어 있는데, 이거 체크 안 하면 매번 콘솔에서 conda 인식 안 됨 — 반드시 체크)
4. 설치 완료 후 **PowerShell 완전히 재시작**

#### 3. 확인
```powershell
conda --version
```

#### 4. 환경 생성 (여기부터는 Mac과 동일)
```powershell
conda create -n doit python=3.11 -y
conda activate doit
```

## ✅ 작업 규칙

1. 자기 폴더만 수정. `answer/` 와 남의 폴더는 건드리지 않는다.
2. push 전 반드시 pull.
3. 커밋 메시지는 어디를 했는지 명시. 예) `chap05/hyeonsoo: 재귀 hanoi 구현`
4. push가 거부(rejected)되면: `git pull --rebase` → `git push`

## 🔧 Git 워크플로우 (Do It 버전 — 이거면 충분함)

브랜치 없이 각자 폴더에서만 작업하니까 아래 4단계만 반복하면 됨:

```bash
git pull                          # 시작 전 항상
# chapXX/본인이름/ 안에서 실습 코드 작성
git add .
git commit -m "chapXX/이름: 내용"
git push
```

push가 거부(rejected)되면:
```bash
git pull --rebase
git push
```

첫 push 시 GitHub이 비밀번호 대신 **Personal Access Token(PAT)**을 요구할 수 있음.
GitHub Settings → Developer settings → Personal access tokens → Generate new token (repo 권한 체크) 에서 발급.

<details>
<summary>📚 심화 Git 명령어 정리 (브랜치/PR/롤백 — 지금 Do It엔 불필요, 나중에 팀 프로젝트용)</summary>

# 📌 Git 팀 프로젝트 필수 명령어 정리

## 1️⃣ `git branch`
현재 로컬에 존재하는 브랜치 목록을 보여준다. 자신이 어떤 브랜치 위에 있는지도 확인 가능.
**왜 쓰냐:** 지금 무슨 브랜치에서 작업 중인지 모르면 그게 사고의 시작이다.

## 2️⃣ `git branch -a`
로컬 + 원격(origin)의 모든 브랜치를 다 보여준다.
**왜 쓰냐:** GitHub에서 만든 브랜치가 로컬에 없을 때 이걸로 존재 유무를 확인한다.

## 3️⃣ `git status`
현재 상태 출력 (수정된 파일 / 스테이징 여부 / 커밋 전인지 / 머지 중인지).
**왜 쓰냐:** 작업하기 전에 항상 해야 하는 "건강검진". 여기서 이상 있으면 절대 merge/pull 하지 말 것. 계속 써주면서 확인 필수!

## 4️⃣ `git checkout 브랜치명`
해당 브랜치로 이동. 브랜치가 로컬에 없으면 오류 뜬다. 그럴 땐:
```bash
git checkout -b feature/login origin/feature/login
```

## 5️⃣ `git fetch`
원격(origin)의 최신 커밋/브랜치 정보를 로컬로 가져온다. 단, 현재 작업 브랜치 코드는 전혀 안 바뀐다(초기화 아님).
**왜 쓰냐:** GitHub에서 새 브랜치 만들었는데 로컬에 안 보일 때 / 팀원이 push했는데 checkout·pull이 안 먹을 때.

## 6️⃣ `git pull origin 브랜치명`
원격 브랜치 코드를 받아와서 내 브랜치에 merge. 자기 작업 브랜치를 origin과 맞출 땐 `git pull origin 본인브랜치`.
**주의:** 작업 중인 파일 있을 때 pull하면 충돌 가능 → commit이나 stash로 먼저 정리.

## 7️⃣ `git add .`
변경된 파일 전체를 staging 영역으로. 하기 전/후로 `git status`로 확인 습관화.

## 8️⃣ `git commit -m "메시지"`
staging된 파일을 하나의 "버전"으로 저장 (로컬에만). 대략 `chore` = 파일만 추가, `feat` = 코드 추가, `fix` = 오류 수정.

## 9️⃣ `git push origin 브랜치명`
로컬 커밋들을 GitHub로 올림. 쌓인 커밋 전부 origin에 올라가고, 브랜치는 항상 최신 커밋을 가리킴.
**중요:** 항상 `origin feature/**`로 push. dev/main 직접 push 금지.

## 🔟 `git merge origin/dev`
내 브랜치(feature)에 dev 최신 내용을 합침. pull = 자기 작업 브랜치 최신화, merge = 자기 브랜치 push 전 dev 반영. 이전엔 fetch 먼저.

## 1️⃣1️⃣-1 `git stash`
커밋하기 싫은 작업물을 잠깐 숨기기. origin/dev를 merge해야 하는데 지금 작업 중인 내용이 지저분할 때 사용.

## 1️⃣1️⃣-2 `git stash pop`
stash로 숨긴 내용을 다시 꺼냄. dev merge 후 pop하면 가끔 충돌 날 수 있으니 `git status` 보면서 처리.

## 1️⃣2️⃣ `git reset --hard origin/브랜치명`
로컬 변경사항 싹 버리고 origin 기준으로 초기화. 정말 망했을 때만.

## 1️⃣3️⃣ `git log --oneline`
커밋 히스토리를 한 줄씩 보기. enter/space로 계속 스크롤.

## 1️⃣4️⃣ `git switch 브랜치명`
checkout과 같은 기능.

## 1️⃣5️⃣ `git show 커밋주소:파일경로`
예: `git show 217161c:LongLife/python-agent/app.py`
해당 커밋 시점의 파일 내용을 보고 복사 가능.

## 1️⃣6️⃣ `git tag v1.0-local`
현재 커밋(HEAD)에 "v1.0-local"이라는 이름표를 붙임. "여기까지 상태를 특별히 보관/북마크"하는 개념.

## 1️⃣7️⃣ `git push origin dev --tags`
태그는 로컬에만 존재하므로 GitHub에 올리려면 push 필요. `--tags`는 로컬의 모든 태그를 원격에 업로드.

---

### 🧩 팀플 필수 루틴 요약

**1. 작업 시작 (본인 브랜치)**
```bash
git status
git fetch
git checkout feature/내브랜치
git pull origin feature/내브랜치
```

**2. 작업 마치고 push (본인 브랜치에만)**
```bash
git status
git add .
git status
git commit -m "내용"
git push origin feature/내브랜치
```

**3. PR 만들기 전**
```bash
git status                     # 커밋할 거 있으면 커밋 후 push, status 깨끗해야 함
git fetch
git merge origin/dev
# 충돌 해결
git push                        # 본인 작업 브랜치
```

**4. PR 할 때** — 담당자 호출

**5. Rollback Manual**

스냅샷 저장:
```bash
git checkout dev
git add .
git commit -m "chore: snapshot before aws deploy"
git tag v1.0-local
git push origin dev --tags
```

완전 초기화 (히스토리도 되돌림):
```bash
git checkout dev
git reset --hard v1.0-local
git push origin dev --force
```

히스토리 유지하며 결과만 되돌리기 (협업자와 충돌 최소화):
```bash
git checkout dev
git revert v1.0-local..HEAD
git commit -m "rollback to v1.0-local via revert"
git push origin dev
```

특정 파일만 되돌리기:
```bash
git checkout v1.0-local -- LongLife/python-agent/app.py
git commit -m "restore app.py from v1.0-local"
git push origin dev
```

</details>

## 🗓 운영 방식

- 기간: 7/6(월) ~ 8/28(금), 평일(월~금)
- 월~목: 매일 1주제 진도 (전날 예습 권장)
- 금: 새 진도 없음. 그 주 복습 + 코딩테스트 5문제 + 노션 보고
- 주말: 밀린 진도 따라잡기 + 벽 구간(🧱) 유사문제 (새 진도 X)
- 월요일은 항상 새 주차로 리셋 (밀림을 다음 주로 넘기지 않음)
- 🧱 = 난이도 벽 (주말 복습 권장) / 💤 = 밀리면 자습 전환 가능

## 📅 8주 진도표

### 1주차 (7/6~7/10) 기초 + 배열
- 월 7/6  | 01-1 알고리즘이란 (p.15~30)
- 화 7/7  | 01-2 반복 알고리즘 (p.31~60)
- 수 7/8  | 02-1 자료구조와 배열 (p.61~74)
- 목 7/9  | 02-2 배열 실전: 최댓값/역순/기수변환 (p.75~96)
- 금 7/10 | 02-2 소수 나열 (p.97~107) + 복습 + 코테

### 2주차 (7/13~7/17) 검색 + 해시
- 월 7/13 | 03-1,2 선형검색 + 보초법 (p.109~119)
- 화 7/14 | 03-3 이진검색 + 복잡도 (p.120~130)
- 수 7/15 | 03-4 해시법: 체인법 (p.131~143) 🧱
- 목 7/16 | 03-4 해시법: 오픈주소법 (p.144~152) 🧱
- 금 7/17 | 복습 + 코테

### 3주차 (7/20~7/24) 스택/큐 + 재귀
- 월 7/20 | 04-1 스택 (p.154~167)
- 화 7/21 | 04-2 큐 + 링버퍼 (p.168~184)
- 수 7/22 | 05-1 재귀 기본: 팩토리얼/유클리드 (p.185~191)
- 목 7/23 | 05-2 재귀 분석: 비재귀 표현 (p.192~199)
- 금 7/24 | 복습 + 코테

### 4주차 (7/27~7/31) 재귀 벽
- 월 7/27 | 05-3 하노이의 탑 (p.200~203)
- 화 7/28 | 05-4 8퀸: 퀸 배치/분기 (p.204~214) 🧱
- 수 7/29 | 05-4 8퀸: 분기한정법/구현 (p.212~218) 🧱
- 목 7/30 | 06-1,2 정렬 개론 + 버블/셰이커 (p.219~236)
- 금 7/31 | 복습 + 코테

### 5주차 (8/3~8/7) 정렬 전반
- 월 8/3  | 06-3,4 선택/삽입 정렬 (p.237~246)
- 화 8/4  | 06-5 셸 정렬 (p.247~254)
- 수 8/5  | 06-6 퀵정렬: 분할/기본 (p.255~263) 🧱
- 목 8/6  | 06-6 퀵정렬: 비재귀/피벗/복잡도 (p.264~276) 🧱
- 금 8/7  | 복습 + 코테

### 6주차 (8/10~8/14) 정렬 벽 + 문자열
- 월 8/10 | 06-7 병합정렬 (p.277~285)
- 화 8/11 | 06-8 힙정렬 (p.286~296) 🧱
- 수 8/12 | 06-9 도수정렬 (p.297~304) 💤
- 목 8/13 | 07-1 브루트포스 문자열검색 (p.305~309)
- 금 8/14 | 복습 + 코테

### 7주차 (8/17~8/21) 문자열 벽 + 리스트
- 월 8/17 | 07-2 KMP 실패함수 (p.310~314) 🧱 (최대 난코스)
- 화 8/18 | 07-3 보이어·무어 (p.315~320) 💤
- 수 8/19 | 08-1,2 연결리스트 + 포인터 (p.321~342)
- 목 8/20 | 08-3 커서 연결리스트 (p.343~355) 🧱 💤
- 금 8/21 | 복습 + 코테

### 8주차 (8/24~8/28) 리스트 마무리 + 트리
- 월 8/24 | 08-4 원형이중 연결리스트 (p.356~376) 💤
- 화 8/25 | 09-1 트리 구조/용어 (p.377~381)
- 수 8/26 | 09-2 이진트리 + 이진검색트리 (p.382~397) 🧱
- 목 8/27 | 09-2 이진검색트리 구현 (p.398~400) 🧱
- 금 8/28 | 전체 복습 + 최종 코테

## ⚠️ 밀림 대응 우선순위

심하게 밀리면 아래 순서로 모임 스킵 → 개인 자습 전환 (트리를 지키기 위한 완충재)

1. 06-9 도수정렬 (코테 비중 낮음)
2. 07-3 보이어·무어 (KMP만 확실하면 자습 가능)
3. 08-3 커서 연결리스트 (파이썬 코테 거의 안 나옴)
4. 08-4 원형이중 연결리스트 (개념만, 구현은 자습)

## 👥 참여자

- hyeonsoo
- hyeonjin
- bumkwan
- younghyeon
- eunseong
