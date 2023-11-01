# CRUD(Create Read Update Delete) 로직
- 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리기능

## 프로젝트 구조 작성
1. 프로젝트 폴더 생성
2. 프로젝트 폴더 vscode로 열기
    - `.gitignore`, `README.md`
3. 장고 새로운 프로젝트 생성
```
django-admin startproject <projectname> .
```
4. 가상환경 설정, 활성화
```python
# 파이썬 모듈 venv을 'venv'이름으로 실행
python -m venv venv
# 가상환경 활성화
source venv/Scripts/activate
```
    - (venv)가 터미널에 표시되는지 확인
5. 가상환경에 장고설치
```
pip install django
```
6. 서버실행확인
```
python manage.py runserver
```
7. 앱생성
```python
django-admin startapp <appname>
```
8. 앱등록
`setting.py`의 `INSTALLED_APP`리스트에 앱이름 추가