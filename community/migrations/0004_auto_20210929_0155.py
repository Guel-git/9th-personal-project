# Generated by Django 3.1.7 on 2021-09-28 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_auto_20210929_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community_reply',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_replys', to='community.community'),
        ),
    ]
