

from rest_framework import status
from .models import Game, GameCategory, PlayerScore, Player
from .serializers import GameSerializer, GameCategorySerializer,PlayerSerializer,PlayerScoreSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics

# Create your views here.




class GameCategoryList(generics.ListCreateAPIView):
    queryset= GameCategory.objects.all()
    serializer_class = GameCategorySerializer




class GameCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    


class GameList(generics.ListCreateAPIView):
    queryset= Game.objects.all()
    serializer_class = GameSerializer
    


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    


class PlayerList(generics.ListCreateAPIView):
    queryset =  Player.objects.all()
    serializer_class = PlayerSerializer
    


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    


class PlayerScoreList(generics.ListCreateAPIView):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    

class PlayerScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= PlayerScoreSerializer
    serializer_class = PlayerScoreSerializer



class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self,request, *args, **kwargs):
        return Response({
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