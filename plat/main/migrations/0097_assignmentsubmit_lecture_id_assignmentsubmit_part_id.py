# Generated by Django 4.1.7 on 2024-08-15 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0096_assignmentsubmit_assignment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentsubmit',
            name='lecture_id',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='assignmentsubmit',
            name='part_id',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
