# Generated by Django 4.0.4 on 2022-05-27 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_digipet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digipet',
            name='mood',
            field=models.CharField(default='hungry', max_length=20),
        ),
    ]
