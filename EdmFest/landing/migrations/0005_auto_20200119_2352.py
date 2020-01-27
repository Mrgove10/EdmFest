# Generated by Django 2.2.9 on 2020-01-19 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_auto_20200119_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='picture',
            field=models.ImageField(
                default='Artist Image', upload_to='cdn/images/artists'),
        ),
        migrations.AlterField(
            model_name='festival',
            name='picture',
            field=models.ImageField(
                default='Festival Image', upload_to='cdn/images/festivals'),
        ),
    ]