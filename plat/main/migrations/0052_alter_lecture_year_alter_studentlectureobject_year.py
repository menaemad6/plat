# Generated by Django 4.1.7 on 2024-07-29 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0051_profile_no_of_sells'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='year',
            field=models.CharField(choices=[('first', 'First'), ('second', 'Second'), ('third', 'Third')], default='first', max_length=25),
        ),
        migrations.AlterField(
            model_name='studentlectureobject',
            name='year',
            field=models.CharField(choices=[('first', 'First'), ('second', 'Second'), ('third', 'Third')], default='first', max_length=25),
        ),
    ]
