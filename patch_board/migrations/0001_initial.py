# Generated by Django 2.2.7 on 2019-11-26 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patch_board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('created_date', models.DateField(blank=True, null=True)),
                ('memo', models.CharField(blank=True, max_length=1000)),
                ('hits', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
