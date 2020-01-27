# Generated by Django 2.2.9 on 2020-01-27 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0011_auto_20200127_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='added_by',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='artist',
            name='born',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='contry_origin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='died',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='is_active',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='festival',
            name='added_by',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='festival',
            name='contry',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='festival',
            name='last_year',
            field=models.PositiveIntegerField(default=''),
        ),
    ]
