# Generated by Django 4.1.7 on 2023-04-21 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("comun", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Usuario",
            ),
        ),
    ]
