# Generated by Django 2.2.6 on 2019-10-12 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectinfo', '0006_projectinfo_date_of_approval'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectinfo',
            name='Recommended',
        ),
    ]
