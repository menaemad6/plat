# Generated by Django 4.1.7 on 2024-07-31 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0066_group_last_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='image',
        ),
    ]
