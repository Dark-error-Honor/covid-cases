# Generated by Django 3.0.8 on 2020-08-02 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('num', models.IntegerField()),
                ('confirmed', models.IntegerField()),
                ('active', models.IntegerField()),
                ('deaths', models.IntegerField()),
                ('recovered', models.IntegerField()),
            ],
        ),
    ]
