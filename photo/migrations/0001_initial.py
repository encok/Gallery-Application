# Generated by Django 3.2.8 on 2021-10-08 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=30)),
                ('image_name', models.CharField(max_length=30)),
                ('image_description', models.CharField(max_length=50)),
            ],
        ),
    ]
