# Generated by Django 4.2.2 on 2023-06-15 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_projectsweb_projectno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(max_length=1000)),
                ('img', models.ImageField(upload_to='')),
                ('detailbtn', models.CharField(max_length=200)),
                ('backbBtn', models.CharField(max_length=200)),
                ('projectID', models.IntegerField()),
            ],
        ),
    ]
