# Generated by Django 3.0.8 on 2020-08-02 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldnums', '0003_auto_20200802_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='active',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='country',
            name='confirmed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='country',
            name='deaths',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='country',
            name='recovered',
            field=models.IntegerField(default=0),
        ),
    ]