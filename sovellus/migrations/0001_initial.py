# Generated by Django 4.1.6 on 2023-02-06 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postaus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otsikko', models.CharField(max_length=200)),
                ('teksti', models.TextField()),
            ],
        ),
    ]
