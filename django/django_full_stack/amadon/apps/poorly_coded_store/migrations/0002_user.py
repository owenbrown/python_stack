# Generated by Django 2.2.1 on 2019-05-31 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poorly_coded_store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('password_hash', models.CharField(max_length=1023)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
    ]
