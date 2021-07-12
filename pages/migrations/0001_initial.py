# Generated by Django 3.2.5 on 2021-07-12 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=100, verbose_name='Nom')),
                ('firstname', models.CharField(max_length=100, verbose_name='Prénom')),
                ('designation', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('facebook_link', models.URLField()),
                ('twitter_link', models.URLField()),
                ('google_link', models.URLField()),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date creation')),
            ],
        ),
    ]