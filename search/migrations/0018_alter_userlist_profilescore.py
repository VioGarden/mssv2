# Generated by Django 4.1 on 2022-09-12 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0017_userlist_profilescore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlist',
            name='ProfileScore',
            field=models.ForeignKey(blank=True, default='--', null=True, on_delete=django.db.models.deletion.CASCADE, to='search.songscore'),
        ),
    ]
