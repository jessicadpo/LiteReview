# Generated by Django 5.0.2 on 2024-03-21 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litereview', '0003_alter_review_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.CharField(max_length=9999, null=True),
        ),
    ]
