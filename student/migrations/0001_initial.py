# Generated by Django 4.1 on 2022-09-26 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rno', models.IntegerField()),
                ('name', models.CharField(max_length=15)),
                ('marks', models.IntegerField()),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=15)),
                ('dob', models.CharField(max_length=15)),
                ('role',models.CharField(max_length=10)),
            ],
        ),
    ]