from django.db import models

# Create your models here.
class UserType(models.Model):
    type_name = models.CharField(max_length=255)

    def __str__(self):
        return self.type_name

class User(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

class PlayerInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.BigIntegerField()
    nb_of_wins = models.BigIntegerField()

    def __str__(self):
        return f"{self.user.username} - level: {self.level}"

class Match(models.Model):
    player_1 = models.ForeignKey(PlayerInfo, related_name='player_1_matches', on_delete=models.CASCADE)
    player_2 = models.ForeignKey(PlayerInfo, related_name='player_2_matches', on_delete=models.CASCADE)
    player_1_score = models.BigIntegerField()
    player_2_score = models.BigIntegerField()
    winner_player = models.ForeignKey(PlayerInfo, related_name='won_matches', on_delete=models.CASCADE)

    def __str__(self):
        return f"Match {self.id} - Winner: {self.winner_player}"
