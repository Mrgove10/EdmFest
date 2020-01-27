from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# for images : https://docs.djangoproject.com/fr/2.2/topics/files/
# https://stackoverflow.com/questions/18632566/admin-filefield-current-url-incorrect
# https://stackoverflow.com/questions/5871730/how-to-upload-a-file-in-django/8542030#8542030
class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    #picture = models.ImageField(upload_to='artists', default='Artist Image')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    born = models.DateField(null=False,default='')
    contry_origin = models.CharField(max_length=100)
    description = models.CharField(max_length=2048,null=False,default='')
    died = models.DateField()
    first_name = models.CharField(max_length=150,null=False,default='')
    is_active = models.BooleanField()
    last_name = models.CharField(max_length=150)
    stage_name = models.CharField(max_length=150,null=False,default='')
    
    def __str__(self):
        return self.stage_name


class Festival(models.Model):
    id = models.AutoField(primary_key=True)
    #picture = models.ImageField(upload_to='festivals', default='Festival Image')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    contry = models.CharField(max_length=100)
    description = models.CharField(max_length=2048,null=False,default='')
    first_year = models.PositiveIntegerField()
    headliners = models.ManyToManyField(Artist)
    last_year = models.PositiveIntegerField()
    location_lat = models.FloatField()
    location_lng = models.FloatField()
    location_name = models.CharField(max_length=150)
    name = models.CharField(max_length=150,null=False)
    youtube_chanel = models.CharField(max_length=2048)
    
    def __str__(self):
        return self.name
