"""SnakeGame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from base.views import StartGame, userinp, update_score, leaderboard,download_csv


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", userinp, name="usrinp"),
    path("user_input", userinp, name="usrinp"),
    path("startgame/<int:id>",StartGame,name="game"),
    path("update_score/<int:id>",update_score,name="update_score"),
    path('leaderboard', leaderboard, name='leaderboard'),
    path('download_csv', download_csv, name='download_csv'),
]

