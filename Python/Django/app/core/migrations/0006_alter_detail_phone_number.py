# Generated by Django 4.2.16 on 2024-11-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_detail_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='Phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
