# Generated by Django 3.1.2 on 2021-09-07 11:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('venue', models.CharField(max_length=254)),
                ('name', models.CharField(max_length=254)),
                ('tagline', models.TextField(max_length=500)),
                ('vanue_page_link', models.URLField(max_length=500)),
                ('organiser_website', models.URLField(max_length=500)),
                ('organiser_email', models.EmailField(max_length=254)),
                ('website', models.URLField(max_length=500)),
                ('type', models.TextField()),
                ('category', models.TextField()),
                ('business_category', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('linkedin', models.URLField(blank=True, max_length=500, null=True)),
                ('twitter', models.URLField(blank=True, max_length=500, null=True)),
                ('facebook', models.URLField(blank=True, max_length=500, null=True)),
                ('instagram', models.URLField(blank=True, max_length=500, null=True)),
                ('youtube', models.URLField(blank=True, max_length=500, null=True)),
                ('tiktok', models.URLField(blank=True, max_length=500, null=True)),
                ('hashtag', models.CharField(max_length=200)),
                ('mention', models.CharField(max_length=200)),
                ('visitors_number', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('exhibitors_number', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('description', models.TextField(max_length=1000)),
                ('logo', models.ImageField(blank=True, max_length=500, upload_to='')),
            ],
        ),
    ]
