# Generated by Django 3.1.7 on 2021-09-28 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_community_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community_reply',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replys', to='community.community'),
        ),
    ]
