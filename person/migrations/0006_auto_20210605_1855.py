# Generated by Django 3.2.4 on 2021-06-05 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0005_auto_20210605_0045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='news',
            name='subtitle',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
