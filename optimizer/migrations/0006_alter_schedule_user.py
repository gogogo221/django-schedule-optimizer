# Generated by Django 4.2.1 on 2023-07-07 02:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("optimizer", "0005_alter_schedule_course_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schedule",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="schedules",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]