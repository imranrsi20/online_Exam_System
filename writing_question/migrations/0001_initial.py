# Generated by Django 3.1.7 on 2021-05-15 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Writen_Exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='W_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Writen_Exam.examinfo')),
            ],
        ),
        migrations.CreateModel(
            name='W_Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200)),
                ('mark', models.FloatField(blank=True, default=0.0, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='writing_question.w_question')),
            ],
        ),
    ]
