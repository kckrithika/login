# Generated by Django 2.0.7 on 2018-07-27 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('_username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('_password', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
    ]