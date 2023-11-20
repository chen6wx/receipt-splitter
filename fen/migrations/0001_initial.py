# Generated by Django 4.2.5 on 2023-11-15 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
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
                ("item_name", models.CharField(max_length=200)),
                (
                    "item_cost",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("num_split", models.IntegerField(default=0)),
                (
                    "split_cost",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Receipt",
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
                ("restaurant_name", models.CharField(max_length=200)),
                ("total_people", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Person",
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
                ("name", models.CharField(max_length=200)),
                (
                    "total_spent",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="fen.item"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="item",
            name="receipt",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="fen.receipt"
            ),
        ),
    ]
