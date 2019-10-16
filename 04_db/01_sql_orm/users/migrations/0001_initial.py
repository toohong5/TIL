# Generated by Django 2.2.6 on 2019-10-16 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('country', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
                ('balance', models.IntegerField()),
            ],
        ),
    ]
