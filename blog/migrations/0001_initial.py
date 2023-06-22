# Generated by Django 4.1.3 on 2023-06-22 17:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=255)),
                ('titulo', models.CharField(max_length=255)),
                ('subtitulo', models.CharField(max_length=255)),
                ('conteudo', models.TextField()),
                ('data_publicacao', models.DateTimeField(default=datetime.datetime(2023, 6, 22, 17, 50, 27, 940046))),
            ],
        ),
    ]
