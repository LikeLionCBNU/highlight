# Generated by Django 3.1.1 on 2020-10-03 17:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editor', models.CharField(max_length=100)),
                ('customer', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('send_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
