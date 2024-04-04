# Generated by Django 3.2.20 on 2024-04-04 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('nickname', models.CharField(max_length=32)),
                ('pwd', models.CharField(max_length=128)),
            ],
        ),
    ]