# Generated by Django 3.1.14 on 2022-02-06 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jamoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(upload_to='Jamoarasm/')),
                ('ism', models.CharField(max_length=234)),
                ('soha', models.CharField(max_length=234)),
                ('rasm1', models.ImageField(upload_to='Jamoarasm/')),
                ('ism1', models.CharField(max_length=234)),
                ('soha1', models.CharField(max_length=234)),
                ('rasm2', models.ImageField(upload_to='Jamoarasm/')),
                ('ism2', models.CharField(max_length=234)),
                ('soha2', models.CharField(max_length=234)),
            ],
        ),
    ]