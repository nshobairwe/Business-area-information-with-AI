# Generated by Django 4.2.5 on 2023-09-21 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mkoa', models.CharField(max_length=100)),
                ('Wilaya', models.CharField(max_length=100)),
                ('Jamii', models.CharField(max_length=100)),
                ('Mtaa', models.CharField(max_length=100)),
            ],
        ),
    ]