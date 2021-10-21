from .permissions import IsOwnerOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework import status
from .models import Game, GameCategory, PlayerScore, Player
from .serializers import GameSerializer, GameCategorySerializer,PlayerSerializer,PlayerScoreSerializer,UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import ScopedRateThrottle

from django_filters import rest_framework as filters
from django_filters import NumberFilter,DateTimeFilter, AllValuesFilter


# Create your views here.
User = get_user_model()



class GameCategoryList(generics.ListCreateAPIView):
    queryset= GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    throttle_scope = 'game-categories'
    throttle_classes = (ScopedRateThrottle,)




class GameCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    throttle_scope = 'game-categories'
    throttle_classes = (ScopedRateThrottle,)
    filter_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name',)    


class GameList(generics.ListCreateAPIView):
    queryset= Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsOwnerOrReadOnly,IsAuthenticatedOrReadOnly]
    filter_fields = ('name','game_category','release_date','played','owner',)
    search_fields = ('^name',)
    ordering_fields = ('name', 'release_date',)


    def perform_create(self, serializer):
        serializer.save(owner= self.request.user)


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsOwnerOrReadOnly,IsAuthenticatedOrReadOnly]





class PlayerList(generics.ListCreateAPIView):
    queryset =  Player.objects.all()
    serializer_class = PlayerSerializer
    filter_fields = ('name','gender',)
    search_fields = ('^name',)
    ordering_fields = ('name',)


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    




class PlayerScoreFilter(filters.FilterSet):

    min_score = NumberFilter( field_name = 'score_board', lookup_expr = 'gte')
    max_score = NumberFilter( field_name='score_board', lookup_expr='lte')
    from_date = DateTimeFilter(field_name='score_date', lookup_expr='gte')
    to_date = DateTimeFilter(field_name='score_date', lookup_expr='lte')
    player_name = AllValuesFilter(field_name='player__name')
    game_name = AllValuesFilter(field_name='game__name')

    class Meta:
        model = PlayerScore
        fields = (
            'score_board',
            'from_date',
            'to_date',
            'min_score',
            'max_score',
            'player_name',
            'game_name'
        )





class PlayerScoreList(generics.ListCreateAPIView):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    filter_class = PlayerScoreFilter
    ordering_fields = ('score_board','score_date',)
    

class PlayerScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= User.objects.all()
    serializer_class = UserSerializer




class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self,request, *args, **kwargs):
        return Response({
            'user': reverse('user-list', request=request),
            'player': reverse('player-list', request=request),
            'game-category': reverse('gamecategory-list', request=request),
            'games': reverse('game-list', request=request),
            'scores': reverse('playerscore-list', request=request)
        })










































# @api_view(['GET','POST'])
# def game_list(request):
#     if request.method == 'GET':
#         games = Game.objects.all()
#         game_serializer = GameSerializer(games, many=True)
#         return Response(game_serializer.data)



#     elif request.method == 'POST':
        
#         game_serializer = GameSerializer(data=request.data)
#         if game_serializer.is_valid():
#             game_serializer.save()
#             return Response(game_serializer.data, status =status.HTTP_201_CREATED)

#         return Response(game_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])

# def game_detail(request,pk):
#     try:
#         game = Game.objects.get(pk=pk)
#     except Game.DoesNotExist:
#         return Response({'message':'Data does not exists'},status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         game_serializer = GameSerializer(game)
#         return Response(game_serializer.data)

#     elif request.method == 'PUT':
        
#         game_serializer = GameSerializer(game, data=request.data)
#         if game_serializer.is_valid():
#             game_serializer.save()
#             return Response(game_serializer.data,status= status.HTTP_202_ACCEPTED)
#         return Response(game_serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    
#     elif request.method == 'DELETE':
#         game.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)


#