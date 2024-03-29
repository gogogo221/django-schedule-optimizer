# Generated by Django 4.2.1 on 2023-06-04 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("optimizer", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="coursecombo", name="units",),
        migrations.RemoveField(model_name="schedule", name="units",),
        migrations.AlterField(
            model_name="coursecombo",
            name="schedules",
            field=models.ManyToManyField(
                null=True, related_name="course_combos", to="optimizer.schedule"
            ),
        ),
        migrations.AlterField(
            model_name="professor",
            name="difficulty",
            field=models.DecimalField(
                blank=True, decimal_places=1, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="professor",
            name="num_ratings",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="professor",
            name="rating",
            field=models.DecimalField(
                blank=True, decimal_places=1, max_digits=5, null=True
            ),
        ),
    ]
