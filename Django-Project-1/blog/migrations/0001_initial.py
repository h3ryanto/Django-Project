# Generated by Django 3.1.5 on 2021-01-27 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='biodata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=20)),
                ('alamat', models.CharField(max_length=50)),
            ],
        ),
    ]
