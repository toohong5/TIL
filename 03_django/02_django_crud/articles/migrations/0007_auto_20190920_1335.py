# Generated by Django 2.2.5 on 2019-09-20 04:35

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20190920_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='articles/images'),
        ),
    ]
