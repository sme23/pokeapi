# Generated by Django 3.1.14 on 2023-11-21 12:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pokemon_v2", "0013_pokemonabilitypast"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itemsprites",
            name="sprites",
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name="pokemonsprites",
            name="sprites",
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name="pokemonformsprites",
            name="sprites",
            field=models.JSONField(),
        ),
    ]
