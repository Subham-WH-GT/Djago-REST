from django.db import models

# Create your models here.

class PlayerModel(models.Model):
    playerName=models.CharField(max_length=25)
    jerseyNumber=models.IntegerField
    country=models.CharField(max_length=20)

    def __str__(self):
        return self.playerName
