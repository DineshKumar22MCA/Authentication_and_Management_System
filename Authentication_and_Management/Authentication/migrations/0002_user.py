# Generated by Django 5.0.3 on 2024-03-21 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=255)),
                ('admin', models.CharField(max_length=255)),
            ],
        ),
    ]
