# Generated by Django 5.1.5 on 2025-04-14 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0015_alter_userprofile_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='followers',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers', to='space.userprofile'),
        ),
    ]
