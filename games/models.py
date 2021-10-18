from django.db import models
from django.db.models.fields import CharField, DateTimeField

# Create your models here.

class GameCategory(models.Model):
    name = models.CharField(max_length=250)


    def __str__(self):
        return self.name

class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length= 200, blank=True, default='')
    release_date = models.DateTimeField()
    game_category = models.ForeignKey(GameCategory, related_name='games',on_delete=models.CASCADE)
    played = models.BooleanField(default=False)


    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name



class Player(models.Model):


    GENDER_CHOICES = (
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
    )
    name = models.CharField(max_length=240)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6, default="FEMALE")
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name


class PlayerScore(models.Model):

    player = models.ForeignKey(Player, related_name='scores', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score_board = models.IntegerField()
    score_date = models.DateField(auto_now_add=True)


    class Meta:
        ordering =('-score_board',)