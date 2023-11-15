from django.db import models

# Create your models here.

class HighScore(models.Model):
    score = models.IntegerField()
    usr_id = models.IntegerField()
    
    def __str__(self):
        return self.score

class ScoreTable(models.Model):
    usr_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, default="other")
    score = models.IntegerField()
    timing = models.IntegerField()

    def __str__(self):
        return f"{self.name} - Score: {self.score} - Time: {self.timing}"
    
