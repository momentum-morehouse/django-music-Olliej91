# Generated by Django 3.1.2 on 2020-10-21 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.CharField(max_length=255)),
                ('artist', models.CharField(max_length=255)),
                ('release', models.DateField(blank=True, null=True)),
                ('genre', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
