# Generated by Django 4.0.4 on 2022-05-31 04:33

from django.db import migrations
import questions.models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0012_delete_questions_question_question_topic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=questions.models.NonStrippingCharField(blank=True, null=True),
        ),
    ]
