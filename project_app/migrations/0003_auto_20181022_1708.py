# Generated by Django 2.1.2 on 2018-10-22 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0002_auto_20181022_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='describe',
            field=models.TextField(max_length=100),
        ),
    ]
