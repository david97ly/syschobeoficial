# Generated by Django 2.0.5 on 2019-09-17 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='codcliente',
            field=models.AutoField(db_column='codcliente_id', primary_key=True, serialize=False),
        ),
    ]
