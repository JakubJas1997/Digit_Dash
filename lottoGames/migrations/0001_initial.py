# Generated by Django 4.2.3 on 2023-08-05 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OneOutOfTwenty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('luckyNumber', models.IntegerField()),
            ],
        ),
    ]