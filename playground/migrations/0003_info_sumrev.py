# Generated by Django 4.1.2 on 2022-11-22 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_delete_websiteuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='sumRev',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
