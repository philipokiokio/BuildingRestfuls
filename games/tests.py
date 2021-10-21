from django.test import TestCase
from django.urls import reverse
from django.utils.http import urlencode
from rest_framework import status
from rest_framework.test import APITestCase
from .models import GameCategory



# Create your tests here.

class GameCategoryTests(APITestCase):
    def create_game_category(self,name):
        url = reverse('gamecategory-list')

        data = {'name':name}
        response = self.client.post(url,data, format='json')
        return response

    def test_create_and_retrieve_game_category(self):
        new_game_category_name = 'New Game Category'
        response = self.create_game_category(new_game_category_name)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GameCategory.objects.count(),1)
        self.assertEqual(GameCategory.objects.get().name, new_game_category_name)
        print(f'{GameCategory.objects.get().pk}')

    def test_create_duplicated_game_category(self):
        url = reverse('gamecategory-list')
        new_game_category_name = 'New Game Category'
        data = {'name':new_game_category_name}
        response1 = self.create_game_category(new_game_category_name)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        response2 = self.create_game_category(new_game_category_name)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)


    def test_retrieve_game_categories_list(self):
        new_game_category_name = 'New Game Category'
        self.create_game_category(new_game_category_name)
        url = reverse('gamecategory-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'],1)
        self.assertEqual(response.data['results'][0]['name'], new_game_category_name)


    def test_update_game_category(self):
        """
        Ensure we can update a single field for a game category
        """
        new_game_category_name = 'Initial Name'
        response = self.create_game_category(new_game_category_name)
        url = reverse('gamecategory-detail',None, {response.data['pk']})
        updated_game_category_name = 'Updated Game Category Name'
        data = {'name': updated_game_category_name}
        patch_response = self.client.patch(url, data, format='json')
        self.assertEqual(patch_response.status_code,status.HTTP_200_OK)
        self.assertEqual(patch_response.data['name'],updated_game_category_name)

def test_filter_game_category_by_name(self):
        """
        Ensure we can filter a game category by name
        """
        game_category_name1 = 'First game category name'
        self.create_game_category(game_category_name1)
        game_caregory_name2 = 'Second game category name'
        self.create_game_category(game_caregory_name2)
        filter_by_name = { 'name' : game_category_name1 }
        url = '{0}?{1}'.format(reverse('gamecategory-list'),urlencode(filter_by_name))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'],1)
        self.assertEqual(response.data['results'][0]['name'], game_category_name1)


from games.models import Player


class PlayerTests(APITestCase):
    def create_player(self,name, gender):
        url = reverse('player-list')
        data = {'name': name, 'gender':gender}
        response = self.client.post(url,data, format='json')
        return response

    def test_create_and_retrieve_player(self):

        new_player_name = 'New Player'
        new_player_gender = Player.MALE
        response = self.create_player(new_player_name,new_player_gender)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.asertEqual(Player.objects.count(),1)
        self.assertEqual(Player.objects.get().name, new_player_name)


    def test_create_duplicated_player(self):

        url = reverse('player-list')
        new_player_name = 'New Femal Player'
        new_player_gender = Player.FEMALE
        response1 = self.create_player(new_player_name,new_player_gender)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        response2 = self.create_player(new_player_name,new_player_gender)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)



    def test_retrieve_players_list(self):

        new_player_name = 'New Female Player'
        new_player_gender = Player.FEMALE
        self.create_player(new_player_name,new_player_gender)
        url = reverse('player-list')
        response = self.client.get(url,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'],1)
        self.assertEqual(response.data['results'][0]['name'], new_player_name)
        self.assertEqual(response.data['results'][0]['gender'], new_player_gender)
        