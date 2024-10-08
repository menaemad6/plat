# Generated by Django 4.1.7 on 2024-08-08 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0089_alter_assignmentsubmit_opened_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question_type',
            field=models.CharField(choices=[('q_choices', 'Q Choices'), ('writing', 'Writing')], default='q_choices', max_length=25),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('q_choices', 'Q Choices'), ('writing', 'Writing')], default='q_choices', max_length=25),
        ),
    ]
