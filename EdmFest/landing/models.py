from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    stage_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    contry_origin = models.CharField(max_length=100)
    born = models.DateField()
    died = models.DateField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.stage_name


class Festival(models.Model):
    id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    location_name = models.CharField(max_length=150)
    contry = models.CharField(max_length=100)
    location_lat = models.FloatField()
    location_lng = models.FloatField()
    first_year = models.PositiveIntegerField()
    last_year = models.PositiveIntegerField()
    youtube_chanel = models.CharField(max_length=2048)
    headliners = models.ManyToManyField(Artist)

    def __str__(self):
        return self.name
