# Generated by Django 3.1.14 on 2022-02-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_delete_animal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123)),
                ('text', models.CharField(max_length=123)),
                ('rasm', models.ImageField(upload_to='title/')),
            ],
        ),
    ]
