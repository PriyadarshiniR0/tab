# Generated by Django 5.1.3 on 2024-12-20 09:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('cno', models.IntegerField(max_length=50)),
                ('cname', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Capital',
            fields=[
                ('capname', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('capno', models.IntegerField(max_length=50)),
                ('cname', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='country.country')),
            ],
        ),
    ]
