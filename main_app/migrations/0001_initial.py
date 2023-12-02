# Generated by Django 4.2.7 on 2023-12-01 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dmodels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='media')),
                ('body', models.TextField()),
            ],
        ),
    ]