# Generated by Django 4.2.5 on 2023-11-16 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fen", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="item",
            old_name="item_name",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="item",
            old_name="item_cost",
            new_name="price",
        ),
    ]
