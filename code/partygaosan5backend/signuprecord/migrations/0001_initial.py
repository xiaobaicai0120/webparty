# Generated by Django 2.0.5 on 2019-11-29 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartyName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('telephone', models.CharField(max_length=11, verbose_name='手机号码')),
            ],
            options={
                'db_table': 'party2020_record',
            },
        ),
    ]