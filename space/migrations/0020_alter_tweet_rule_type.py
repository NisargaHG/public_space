# Generated by Django 5.1.5 on 2025-04-14 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0019_userprofile_post_limit_date_userprofile_posts_today_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='rule_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
