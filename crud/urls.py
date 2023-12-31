"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Read
    path('index/', views.index),
    path('posts/<int:id>/',views.detail),

    # Create(사용자에게 데이터를 입력받고, 저장함)
    path('posts/new/', views.new),
    path('posts/create/', views.create),

    # Delete
    path('posts/<int:id>/delete/', views.delete),

    # Update(수정할 기존 데이터를 READ, 수정데이터 입력받기, 저장)
    path('posts/<int:id>/edit/', views.edit),
    path('posts/<int:id>/updata/', views.update),
]