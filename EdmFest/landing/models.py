from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# for images : https://docs.djangoproject.com/fr/2.2/topics/files/
class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    born = models.DateField(null=False,default='')
    contry_origin = models.CharField(max_length=100)
    description = models.CharField(max_length=2048,null=False,default='')
    died = models.DateField()
    first_name = models.CharField(max_length=150,null=False,default='')
    is_active = models.BooleanField()
    last_name = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='images/artists', default='Artist Image')
    stage_name = models.CharField(max_length=150,null=False,default='')
    
    def __str__(self):
        return self.stage_name


class Festival(models.Model):
    id = models.AutoField(primary_key=True)
    contry = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=2048,null=False,default='')
    first_year = models.PositiveIntegerField()
    headliners = models.ManyToManyField(Artist)
    last_year = models.PositiveIntegerField()
    location_lat = models.FloatField()
    location_lng = models.FloatField()
    location_name = models.CharField(max_length=150)
    name = models.CharField(max_length=150,null=False)
    picture = models.ImageField(upload_to='images/festivals', default='Festival Image')
    youtube_chanel = models.CharField(max_length=2048)
    
    def __str__(self):
        return self.name
