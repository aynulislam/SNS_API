# Generated by Django 2.2.5 on 2019-11-06 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_auto_20191106_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sncontentdetail',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
