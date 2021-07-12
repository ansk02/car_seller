# Generated by Django 3.2.5 on 2021-07-12 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'Equipe', 'verbose_name_plural': 'Equipes'},
        ),
        migrations.AlterField(
            model_name='team',
            name='facebook_link',
            field=models.URLField(verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='team',
            name='google_link',
            field=models.URLField(verbose_name='Google Plus'),
        ),
        migrations.AlterField(
            model_name='team',
            name='twitter_link',
            field=models.URLField(verbose_name='Twitter'),
        ),
    ]
