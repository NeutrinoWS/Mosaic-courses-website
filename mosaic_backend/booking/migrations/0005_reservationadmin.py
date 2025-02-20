# Generated by Django 4.1.6 on 2023-07-29 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("masterclass", "0010_masterclasstype_image"),
        ("booking", "0004_alter_booking_options_alter_booking_attending"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReservationAdmin",
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
                ("guest_name", models.CharField(max_length=30)),
                ("guest_phone", models.CharField(max_length=15)),
                (
                    "attending",
                    models.ForeignKey(
                        help_text="the course this guests is going to attend",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="admin_reservations",
                        to="masterclass.masterclass",
                        verbose_name="course/masterclass",
                    ),
                ),
            ],
        ),
    ]
