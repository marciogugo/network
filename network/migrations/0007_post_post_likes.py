# Generated by Django 4.0.4 on 2022-12-08 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_rename_post_replies_post_post_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_likes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PostHasLikes', to='network.post'),
        ),
    ]
