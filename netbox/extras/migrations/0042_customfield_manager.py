# Generated by Django 3.0.5 on 2020-05-07 21:06

from django.db import migrations
import extras.models.customfields


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0041_tag_description'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customfield',
            managers=[
                ('objects', extras.models.customfields.CustomFieldManager()),
            ],
        ),
    ]