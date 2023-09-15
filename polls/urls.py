from django.urls import path
from .views import GetGame,GetCreateGame,CreateGame,DetailUpdateDestroy


urlpatterns = [
    path('getGame/',GetGame.as_view()),
    path('createGame/',CreateGame.as_view()),
    path('getcreateGame/',GetCreateGame.as_view()),
    path('<int:pk>/',DetailUpdateDestroy.as_view())
]