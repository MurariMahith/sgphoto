# Generated by Django 3.0.7 on 2020-07-18 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200719_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buying',
            name='uname',
        ),
    ]
