# Generated by Django 3.2 on 2022-11-28 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('device', models.CharField(max_length=100)),
                ('vo', models.FloatField()),
                ('cu', models.FloatField()),
                ('active', models.FloatField()),
                ('reactive', models.FloatField()),
                ('apparent', models.FloatField()),
                ('pf', models.FloatField()),
                ('freq', models.FloatField()),
            ],
            options={
                'db_table': 'sensor',
                'managed': False,
            },
        ),
    ]
