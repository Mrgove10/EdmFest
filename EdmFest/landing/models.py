from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# for images : https://docs.djangoproject.com/fr/2.2/topics/files/
# https://stackoverflow.com/questions/18632566/admin-filefield-current-url-incorrect
# https://stackoverflow.com/questions/5871730/how-to-upload-a-file-in-django/8542030#8542030


class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    #picture = models.ImageField(upload_to='artists', default='Artist Image')
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    born = models.DateField(null=True, blank=True)
    contry_origin = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(
        max_length=2048, null=False, default='', blank=False)
    died = models.DateField(null=True, blank=True)
    first_name = models.CharField(
        max_length=150, null=False, default='', blank=False)
    is_active = models.BooleanField(null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    stage_name = models.CharField(
        max_length=150, null=False, default='', blank=False)

    def __str__(self):
        return self.stage_name


class Festival(models.Model):
    id = models.AutoField(primary_key=True)
    #picture = models.ImageField(upload_to='festivals', default='Festival Image')
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    contry = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(
        max_length=2048, null=False, default='', blank=False)
    first_year = models.PositiveIntegerField(blank=True, null=True)
    headliners = models.ManyToManyField(Artist, blank=True)
    last_year = models.PositiveIntegerField(
        null=False, default='', blank=False)
    location_lat = models.FloatField(null=True, blank=True)
    location_lng = models.FloatField(null=True, blank=True)
    location_name = models.CharField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=150, null=False, blank=False)
    youtube_chanel = models.CharField(max_length=2048, blank=True, null=True)

    def __str__(self):
        return self.name
