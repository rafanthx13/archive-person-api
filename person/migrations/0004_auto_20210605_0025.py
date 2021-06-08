# Generated by Django 3.2.4 on 2021-06-05 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_alter_person_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='news_tags',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='persons_tags',
        ),
        migrations.AddField(
            model_name='news',
            name='news_tags',
            field=models.ManyToManyField(blank=True, to='person.Tag'),
        ),
        migrations.AddField(
            model_name='person',
            name='persons_tags',
            field=models.ManyToManyField(blank=True, to='person.Tag'),
        ),
    ]
