# Generated by Django 4.0.4 on 2022-05-18 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_remove_comment_post_remove_feed_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_tweet', to='feed.feed'),
        ),
        migrations.AddField(
            model_name='feed',
            name='post',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feed.feed'),
        ),
    ]
