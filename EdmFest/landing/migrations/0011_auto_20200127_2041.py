# Generated by Django 2.2.9 on 2020-01-27 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0010_auto_20200127_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='added_by',
            field=models.ForeignKey(
                blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='artist',
            name='contry_origin',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='artist',
            name='died',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='is_active',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='last_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='festival',
            name='contry',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='festival',
            name='first_year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='festival',
            name='headliners',
            field=models.ManyToManyField(
                blank=True, null=True, to='landing.Artist'),
        ),
        migrations.AlterField(
            model_name='festival',
            name='location_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='festival',
            name='location_lng',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='festival',
            name='location_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='festival',
            name='youtube_chanel',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
    ]
