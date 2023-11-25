# Generated by Django 3.2.23 on 2023-11-20 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pesticides', '0007_auto_20231120_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formula',
            name='pesticide_amount',
            field=models.DecimalField(decimal_places=3, max_digits=6, max_length=20, null=True),
        ),
    ]
