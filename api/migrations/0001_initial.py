# Generated by Django 4.1.2 on 2022-11-03 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "contactNo",
                    models.BigIntegerField(primary_key=True, serialize=False),
                ),
                ("firstName", models.CharField(max_length=50)),
                ("middleName", models.CharField(blank=True, max_length=50)),
                ("lastName", models.CharField(blank=True, max_length=50)),
                ("dob", models.DateField()),
                ("gender", models.CharField(max_length=6)),
                ("houseNo", models.CharField(max_length=10)),
                ("streetName", models.CharField(max_length=50)),
                ("localityName", models.CharField(max_length=50)),
                ("cityName", models.CharField(max_length=20)),
                ("countryName", models.CharField(max_length=20)),
                ("pinCode", models.IntegerField()),
                ("kycVerified", models.BooleanField(default=False)),
                ("idImageFront", models.ImageField(upload_to="UserID_front")),
                ("idImageBack", models.ImageField(upload_to="UserID_back")),
                ("userPhoto", models.ImageField(upload_to="UserPhoto")),
            ],
        ),
    ]