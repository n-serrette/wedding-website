# Generated by Django 3.1 on 2020-09-21 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0008_party_response_received'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='invited_dinner',
        ),
    ]
