# Generated by Django 4.2.7 on 2023-12-05 08:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="question",
            old_name="pub_Date",
            new_name="pub_date",
        ),
    ]
