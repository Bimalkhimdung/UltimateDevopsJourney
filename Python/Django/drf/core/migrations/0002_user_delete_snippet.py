# Generated by Django 4.2.16 on 2024-11-14 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=200)),
                ('middlename', models.CharField(blank=True, max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=400)),
                ('phonenumber', models.IntegerField(unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Snippet',
        ),
    ]
