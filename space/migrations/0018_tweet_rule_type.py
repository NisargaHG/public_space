# Generated by Django 5.1.5 on 2025-04-14 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0017_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='rule_type',
            field=models.CharField(choices=[('zero_following_time_rule', 'Zero Following Rule'), ('two_following_limit', 'Two Following Rule'), ('friends_unlimited', 'Friends Rule')], default='two_following_limit', max_length=50),
        ),
    ]
