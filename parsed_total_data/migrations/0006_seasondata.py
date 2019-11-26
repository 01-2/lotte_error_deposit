# Generated by Django 2.2.7 on 2019-11-26 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_total_data', '0005_totaldata_money'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeasonData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.PositiveIntegerField()),
                ('stkOut', models.PositiveIntegerField()),
                ('dbplay', models.PositiveIntegerField()),
                ('homerun', models.PositiveIntegerField()),
                ('balk', models.PositiveIntegerField()),
                ('passedBall', models.PositiveIntegerField()),
                ('error', models.PositiveIntegerField()),
                ('money', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]
