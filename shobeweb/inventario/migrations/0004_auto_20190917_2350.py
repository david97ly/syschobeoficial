# Generated by Django 2.0.5 on 2019-09-17 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_auto_20190917_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturaventa',
            name='codcliente',
            field=models.ForeignKey(blank=True, db_column='codcliente_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Cliente'),
        ),
    ]
