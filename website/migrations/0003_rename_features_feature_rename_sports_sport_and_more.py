# Generated by Django 4.2.13 on 2024-07-09 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_features_news_opinion_sports_delete_article'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='features',
            new_name='feature',
        ),
        migrations.RenameModel(
            old_name='sports',
            new_name='sport',
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'news'},
        ),
    ]
