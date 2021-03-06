# Generated by Django 2.2.9 on 2020-01-19 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_festival_headliners'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='description',
            field=models.CharField(default='', max_length=2048),
        ),
        migrations.AddField(
            model_name='artist',
            name='picture',
            field=models.ImageField(
                default='Artist Image', upload_to='images/artists'),
        ),
        migrations.AddField(
            model_name='festival',
            name='description',
            field=models.CharField(default='', max_length=2048),
        ),
        migrations.AddField(
            model_name='festival',
            name='picture',
            field=models.ImageField(
                default='Festival Image', upload_to='images/festivals'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='born',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='artist',
            name='first_name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='artist',
            name='stage_name',
            field=models.CharField(default='', max_length=150),
        ),
    ]
