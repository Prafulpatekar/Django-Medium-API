# Generated by Django 4.1.7 on 2024-07-08 18:34

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("taggit", "0005_auto_20220424_2025"),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        always_update=True,
                        editable=False,
                        populate_from="title",
                        unique=True,
                    ),
                ),
                (
                    "description",
                    models.CharField(max_length=255, verbose_name="description"),
                ),
                ("body", models.TextField(verbose_name="article content")),
                (
                    "banner_image",
                    models.ImageField(
                        default="/profile_default.png",
                        upload_to="",
                        verbose_name="banner image",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="articles",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at", "-updated_at"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ArticleView",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "viewer_ip",
                    models.GenericIPAddressField(
                        blank=True, null=True, verbose_name="viewer IP"
                    ),
                ),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="article_views",
                        to="articles.article",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user_views",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Article View",
                "verbose_name_plural": "Article Views",
                "unique_together": {("article", "user", "viewer_ip")},
            },
        ),
    ]
