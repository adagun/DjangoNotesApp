# Generated by Django 3.2.6 on 2021-08-13 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20210813_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]
