# Generated by Django 2.2.5 on 2019-10-02 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SnAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(default='Gallery', max_length=100)),
                ('album_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SnAlbumType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SnContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VisibilityMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visibility_mode', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SnContentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_featured', models.BooleanField(default=False)),
                ('is_captcha', models.BooleanField(default=False)),
                ('file', models.FileField(upload_to='')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.SnAlbum')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.SnContentType')),
            ],
        ),
    ]
