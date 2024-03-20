# pylint: skip-file
# Generated by Django 5.0.2 on 2024-03-20 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litereview', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='status',
            field=models.CharField(choices=[('Complete', 'Complete'), ('In Progress', 'In Progress'), ('Dropped', 'Dropped')], default='In Progress', max_length=128),
        ),
    ]
