# Generated by Django 3.0.7 on 2020-07-28 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50)),
                ('post_img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
