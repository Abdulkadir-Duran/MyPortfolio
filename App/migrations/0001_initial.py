# Generated by Django 4.2.2 on 2023-06-15 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField(max_length=500)),
            ],
        ),
    ]
