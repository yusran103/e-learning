# Generated by Django 2.2.6 on 2019-11-20 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0003_auto_20191117_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kuis',
            name='kelas',
        ),
    ]
