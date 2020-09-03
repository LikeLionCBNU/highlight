# Generated by Django 2.1.7 on 2020-09-02 08:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editor', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('production', models.CharField(max_length=20)),
                ('profile', models.ImageField(blank=True, upload_to='')),
                ('grade', models.IntegerField()),
                ('price', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('grade', models.IntegerField()),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Portfolio')),
            ],
        ),
    ]
