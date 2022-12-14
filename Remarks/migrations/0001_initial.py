# Generated by Django 3.1.7 on 2021-05-19 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('question', models.CharField(max_length=250)),
                ('answer', models.TextField()),
                ('mark', models.FloatField(default=0.0)),
            ],
        ),
    ]
