# Generated by Django 4.1.6 on 2023-07-25 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("masterclass", "0010_masterclasstype_image"),
        ("booking", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="attending",
            field=models.ForeignKey(
                help_text="the course this guests is going to attend",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bookings",
                to="masterclass.masterclass",
            ),
        ),
    ]
