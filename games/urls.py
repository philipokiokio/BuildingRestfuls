from django.urls import path
from .views import GameList,GameDetail,GameCategoryList,GameCategoryDetail,PlayerList,PlayerDetail,PlayerScoreList,PlayerScoreDetail,ApiRoot


urlpatterns =[

    path('game-categories/', GameCategoryList.as_view(),name='gamecategory-list'),
    path('game-category/<int:pk>/', GameCategoryDetail.as_view(),name='gamecategory-detail'),
    path('games/', GameList.as_view(),name='game-list'),
    path('games/<int:pk>/', GameDetail.as_view(), name='game-detail'),
    path('players/', PlayerList.as_view(), name='player-list'),
    path('players/<int:pk>/', PlayerDetail.as_view(), name='player-detail'),
    path('player-scores/', PlayerScoreList.as_view(), name='playerscore-list'),
    path('player-score/<int:pk>/', PlayerScoreDetail.as_view(), name='playerscore-detail'),
    path('', ApiRoot.as_view())
]