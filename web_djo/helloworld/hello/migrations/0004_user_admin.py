# Generated by Django 2.1 on 2019-10-30 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_admin',
            fields=[
                ('user_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('psw', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=30)),
            ],
        ),
    ]
