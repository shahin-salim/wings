# Generated by Django 4.0.4 on 2022-06-11 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_comment_post_feed_post_like_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='is_dislike',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dislikes', to='feed.like'),
        ),
        migrations.AlterField(
            model_name='feed',
            name='is_like',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feed.like'),
        ),
    ]