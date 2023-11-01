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
`setting.py`의 `INSTALLED_APP`리스트에 <appname> 추가

9. `urls.py` 수정
- 상단에 `from <앱이름> import views`
- `urlpatterns`리스트에 path('index/',views.index) 추가
10. `views.py` 수정
```python
def index(request):
    return render(request, 'index.html')
```
11. `index.html` 생성
- 원하는대로 생성

## MODEL

1. 모델 정의(`models.py`)
    - 모델의 이름은 기본적으로 단수형태

```python
# 원하는 모델 클래스 만들기
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

```
2. 번역본 생성
```
python manage.py makemigrations
```
3. DB에반영
```python
python manage.py migrate
# DB 반영 확인
python manage.py sqlmigrate posts 0001 
```
4. 생성한 모델을 admin에 등록
```
from .models import Post

admin.site.register(Post)
```
5. 관리자 계정 생성
```
python manage.py createsuperuser
```

## CRUD
> Create, Read, Update, Delete

### 1. READ
- 전체 게시물 출력

```python
from .models import Post

def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)
```
2. index.html

<body>
    <h1>index</h1>
    {% for post in posts%}
        <p>{{post.title}}</p>
        <p>{{post.content}}</p>
        <hr>
    {% endfor %}
</body>

- 하나의 게시물 출력
```python
def detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }
    return render(request, 'detail.html', context)
```
2. detail.html
<body>
    <h1>detail</h1>
    <p>{{post.title}}</p>
    <p>{{post.content}}</p>
</body>

1. views.py