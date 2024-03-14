# Generated by Django 4.1.2 on 2024-03-14 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                ("author", models.CharField(max_length=128)),
                ("datetime", models.DateTimeField(auto_now_add=True)),
                ("rating", models.IntegerField()),
                ("text", models.CharField(max_length=1024)),
                (
                    "media_type",
                    models.CharField(
                        choices=[
                            ("MOV", "Movie"),
                            ("BOK", "Book"),
                            ("MGA", "Manga/Manwha/Manhua"),
                            ("TVS", "TV"),
                            ("MUS", "Music"),
                            ("COM", "Comic/Graphic Novel"),
                        ],
                        default="MOV",
                        max_length=3,
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]