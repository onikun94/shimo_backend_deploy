# Generated by Django 3.2.6 on 2021-12-31 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_air', models.DateField()),
                ('segment', models.TextField()),
                ('address', models.TextField()),
                ('user', models.TextField()),
                ('contents', models.TextField()),
                ('answer', models.TextField()),
                ('pt', models.IntegerField()),
            ],
        ),
    ]
