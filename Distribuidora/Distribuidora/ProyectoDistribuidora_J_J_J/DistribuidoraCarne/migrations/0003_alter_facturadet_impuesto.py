# Generated by Django 4.2.7 on 2023-12-01 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DistribuidoraCarne', '0002_facturadet_impuesto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturadet',
            name='impuesto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='DistribuidoraCarne.impuesto'),
        ),
    ]
