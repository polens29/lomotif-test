# Generated by Django 2.1.5 on 2019-01-09 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20190109_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='playerClass',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
