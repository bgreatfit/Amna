# Generated by Django 2.2.4 on 2019-11-30 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20191201_0108'),
    ]

    operations = [
        migrations.CreateModel(
            name='site_settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(blank=True, max_length=255, null=True)),
                ('logo', models.ImageField(blank=True, upload_to='logo')),
                ('phone_number', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
