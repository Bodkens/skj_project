# Generated by Django 4.2 on 2023-05-06 01:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("store", "0003_alter_game_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="ticket",
            name="consultant",
        ),
        migrations.RemoveField(
            model_name="ticket",
            name="user",
        ),
        migrations.AddField(
            model_name="game",
            name="image",
            field=models.ImageField(null=True, upload_to=""),
        ),
        migrations.DeleteModel(
            name="Consultant",
        ),
        migrations.DeleteModel(
            name="Ticket",
        ),
    ]