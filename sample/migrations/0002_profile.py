# Generated by Django 3.0.5 on 2021-01-20 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('has_kyc', models.BooleanField(default=False)),
                ('military1_service_status', models.CharField(max_length=35)),
            ],
        ),
    ]