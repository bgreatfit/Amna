# Generated by Django 2.2.4 on 2019-11-27 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20191127_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='count_down_ads',
            name='count_down_date',
            field=models.CharField(blank=True, help_text='e.g: 2022/10/01', max_length=255, null=True),
        ),
    ]