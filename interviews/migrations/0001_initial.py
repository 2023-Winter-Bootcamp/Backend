# Generated by Django 4.2.9 on 2024-01-09 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Interview",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("resume", models.IntegerField()),
                ("title", models.CharField(max_length=255)),
                (
                    "style",
                    models.CharField(
                        choices=[
                            ("video", "VIDEO"),
                            ("voice", "VOICE"),
                            ("text", "TEXT"),
                        ],
                        max_length=5,
                    ),
                ),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("frontend", "FRONTEND"),
                            ("backend", "BACKEND"),
                            ("fullstack", "FULLSTACK"),
                        ],
                        max_length=9,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.user"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Interview_Type",
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
                ("type_name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Type_Choice",
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
                (
                    "interview",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="interviews.interview",
                    ),
                ),
                (
                    "interview_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="interviews.interview_type",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Question",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("content", models.CharField(max_length=255)),
                (
                    "question_type",
                    models.CharField(
                        choices=[
                            ("project", "PROJECT"),
                            ("cs", "CS"),
                            ("personality", "PERSONALITY"),
                        ],
                        max_length=11,
                    ),
                ),
                (
                    "interview",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="interviews.interview",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Answer",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("content", models.CharField(max_length=255)),
                ("record_url", models.CharField(max_length=500)),
                (
                    "question",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="interviews.question",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
