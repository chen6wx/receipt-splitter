# Generated by Django 4.2.5 on 2023-11-17 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fen", "0002_rename_item_name_item_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="split_cost",
        ),
    ]