# Generated by Django 3.2.4 on 2021-06-05 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0007_rename_commment_news_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='complete_name',
            field=models.CharField(blank='', max_length=255, null=True),
        ),
    ]