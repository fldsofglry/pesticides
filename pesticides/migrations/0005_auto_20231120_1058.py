# Generated by Django 3.2.23 on 2023-11-20 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pesticides', '0004_auto_20231120_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='formula',
            name='amount',
            field=models.DecimalField(decimal_places=3, max_digits='4', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='formula',
            name='concentration',
            field=models.CharField(choices=[('P', '%'), ('G', '/gallon')], default='P', max_length=2),
        ),
    ]