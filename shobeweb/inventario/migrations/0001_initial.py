# Generated by Django 2.0.5 on 2019-09-17 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('idbodega', models.AutoField(primary_key=True, serialize=False)),
                ('existencias_unidad', models.IntegerField(blank=True, null=True)),
                ('existencias_caja', models.FloatField(blank=True, null=True)),
                ('costo', models.FloatField(blank=True, null=True)),
                ('canticaja', models.FloatField(blank=True, null=True)),
                ('inversion', models.FloatField(blank=True, null=True)),
                ('utilidad', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bodega',
            },
        ),
        migrations.CreateModel(
            name='Cajas',
            fields=[
                ('idcajas', models.AutoField(primary_key=True, serialize=False)),
                ('cajachica', models.FloatField(blank=True, null=True)),
                ('cajagrande', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cajas',
            },
        ),
        migrations.CreateModel(
            name='Categasto',
            fields=[
                ('idcategasto', models.AutoField(primary_key=True, serialize=False)),
                ('gasto', models.CharField(blank=True, max_length=500, null=True)),
                ('tipo', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'categasto',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'categoria',
            },
        ),
        migrations.CreateModel(
            name='Cateingreso',
            fields=[
                ('idcateingreso', models.AutoField(primary_key=True, serialize=False)),
                ('ingreso', models.CharField(blank=True, max_length=500, null=True)),
                ('tipo', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'cateingreso',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('codcliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=250, null=True)),
                ('nit', models.CharField(blank=True, max_length=250, null=True)),
                ('nrc', models.CharField(blank=True, max_length=250, null=True)),
                ('giro', models.CharField(blank=True, max_length=250, null=True)),
                ('direccion', models.CharField(blank=True, max_length=250, null=True)),
                ('telefono', models.CharField(blank=True, max_length=250, null=True)),
                ('fax', models.CharField(blank=True, max_length=250, null=True)),
                ('e_mail', models.CharField(blank=True, max_length=250, null=True)),
                ('estado', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('idclientes', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Configuraciones',
            fields=[
                ('id_config', models.AutoField(primary_key=True, serialize=False)),
                ('tirage_fact', models.CharField(blank=True, max_length=250, null=True)),
                ('tirage_compro', models.CharField(blank=True, max_length=250, null=True)),
                ('tirage_fact_actual', models.CharField(blank=True, max_length=250, null=True)),
                ('tirage_compro_actual', models.CharField(blank=True, max_length=250, null=True)),
                ('numfact', models.CharField(blank=True, max_length=250, null=True)),
                ('numcompro', models.CharField(blank=True, max_length=250, null=True)),
                ('iva', models.DecimalField(blank=True, decimal_places=0, max_digits=8, null=True)),
                ('cotrans', models.DecimalField(blank=True, decimal_places=0, max_digits=8, null=True)),
                ('porce_iva_ret', models.DecimalField(blank=True, decimal_places=0, max_digits=8, null=True)),
            ],
            options={
                'db_table': 'configuraciones',
            },
        ),
        migrations.CreateModel(
            name='Creditos',
            fields=[
                ('idcredito', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.FloatField(blank=True, null=True)),
                ('totalproducto', models.FloatField(blank=True, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('idclientes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Clientes')),
            ],
            options={
                'db_table': 'creditos',
            },
        ),
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('cod_departamento', models.AutoField(primary_key=True, serialize=False)),
                ('departamentos', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'departamentos',
            },
        ),
        migrations.CreateModel(
            name='Detallecompra',
            fields=[
                ('coddetallefacturac', models.AutoField(primary_key=True, serialize=False)),
                ('cantidadunit', models.FloatField(blank=True, null=True)),
                ('descuento', models.FloatField(blank=True, null=True)),
                ('precioreal', models.FloatField(blank=True, null=True)),
                ('preciodescuento', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('total1', models.FloatField(blank=True, null=True)),
                ('preciopublico', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'detallecompra',
            },
        ),
        migrations.CreateModel(
            name='Detallecreditos',
            fields=[
                ('iddetallecreditos', models.AutoField(primary_key=True, serialize=False)),
                ('idcredito', models.IntegerField(blank=True, null=True)),
                ('precio', models.FloatField(blank=True, null=True)),
                ('cantidad', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'detallecreditos',
            },
        ),
        migrations.CreateModel(
            name='Detalledia',
            fields=[
                ('iddetalledia', models.AutoField(primary_key=True, serialize=False)),
                ('idturno', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'detalledia',
            },
        ),
        migrations.CreateModel(
            name='Detallegasto',
            fields=[
                ('iddetallegasto', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('razon', models.CharField(blank=True, max_length=500, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'detallegasto',
            },
        ),
        migrations.CreateModel(
            name='Detalleingreso',
            fields=[
                ('iddetalleingreso', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('razon', models.CharField(blank=True, max_length=500, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'detalleingreso',
            },
        ),
        migrations.CreateModel(
            name='Detallenotacredito',
            fields=[
                ('coddetallenotacredito', models.AutoField(primary_key=True, serialize=False)),
                ('cantidadunit', models.FloatField(blank=True, null=True)),
                ('descuento', models.FloatField(blank=True, null=True)),
                ('precioreal', models.FloatField(blank=True, null=True)),
                ('preciodescuento', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('total1', models.FloatField(blank=True, null=True)),
                ('preciopublico', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'detallenotacredito',
            },
        ),
        migrations.CreateModel(
            name='Detalleventa',
            fields=[
                ('coddetallefacturav', models.AutoField(primary_key=True, serialize=False)),
                ('cantidadunit', models.FloatField(blank=True, null=True)),
                ('descuento', models.FloatField(blank=True, null=True)),
                ('precioreal', models.FloatField(blank=True, null=True)),
                ('preciodescuento', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('total1', models.FloatField(blank=True, null=True)),
                ('preciopublico', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'detalleventa',
            },
        ),
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('iddia', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('numdia', models.IntegerField(blank=True, null=True)),
                ('fechaini', models.DateField(blank=True, null=True)),
                ('horaini', models.TimeField(blank=True, null=True)),
                ('fechafinal', models.DateField(blank=True, null=True)),
                ('horafinal', models.TimeField(blank=True, null=True)),
                ('dianterior', models.FloatField(blank=True, null=True)),
                ('desde', models.IntegerField(blank=True, null=True)),
                ('hasta', models.IntegerField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('activo', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dia',
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id_direcciones', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'direccion',
            },
        ),
        migrations.CreateModel(
            name='Dtncredito',
            fields=[
                ('coddtncredito', models.AutoField(primary_key=True, serialize=False)),
                ('cantidadunit', models.FloatField(blank=True, null=True)),
                ('descuento', models.FloatField(blank=True, null=True)),
                ('precioreal', models.FloatField(blank=True, null=True)),
                ('preciodescuento', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('total1', models.FloatField(blank=True, null=True)),
                ('preciopublico', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dtncredito',
            },
        ),
        migrations.CreateModel(
            name='Facturacompra',
            fields=[
                ('codfacturac', models.AutoField(primary_key=True, serialize=False)),
                ('numfacturac', models.IntegerField(blank=True, null=True)),
                ('tipo', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('sumas', models.FloatField(blank=True, null=True)),
                ('descuento', models.FloatField(blank=True, null=True)),
                ('iva', models.FloatField(blank=True, null=True)),
                ('nosujeta', models.FloatField(blank=True, null=True)),
                ('exentas', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('formadepago', models.CharField(blank=True, max_length=50, null=True)),
                ('unoretencion', models.FloatField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('tiraje', models.CharField(blank=True, max_length=50, null=True)),
                ('fechalimite', models.DateField(blank=True, null=True)),
                ('etilico', models.FloatField(blank=True, null=True)),
                ('advalorem', models.FloatField(blank=True, null=True)),
                ('especifico', models.FloatField(blank=True, null=True)),
                ('bonificacion', models.FloatField(blank=True, null=True)),
                ('descuento1', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'facturacompra',
            },
        ),
        migrations.CreateModel(
            name='Facturaventa',
            fields=[
                ('codfacturav', models.AutoField(primary_key=True, serialize=False)),
                ('numfacturav', models.IntegerField(blank=True, null=True)),
                ('tipo', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('sumas', models.FloatField(blank=True, null=True)),
                ('descuento', models.FloatField(blank=True, null=True)),
                ('iva', models.FloatField(blank=True, null=True)),
                ('nosujeta', models.FloatField(blank=True, null=True)),
                ('exentas', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('formadepago', models.CharField(blank=True, max_length=50, null=True)),
                ('unoretencion', models.FloatField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('tiraje', models.CharField(blank=True, max_length=50, null=True)),
                ('fechavence', models.DateTimeField(blank=True, null=True)),
                ('comision', models.FloatField(blank=True, null=True)),
                ('generada', models.IntegerField(blank=True, null=True)),
                ('efectivo', models.FloatField(blank=True, null=True)),
                ('cambio', models.FloatField(blank=True, null=True)),
                ('usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('hora', models.TimeField(blank=True, null=True)),
                ('turno', models.IntegerField(blank=True, null=True)),
                ('dia', models.IntegerField(blank=True, null=True)),
                ('codcliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Cliente')),
            ],
            options={
                'db_table': 'facturaventa',
            },
        ),
        migrations.CreateModel(
            name='Fechaabono',
            fields=[
                ('idfecha', models.AutoField(primary_key=True, serialize=False)),
                ('iddoc', models.IntegerField(blank=True, null=True)),
                ('fechaabono', models.DateTimeField(blank=True, null=True)),
                ('cantidadabono', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'fechaabono',
            },
        ),
        migrations.CreateModel(
            name='Gastos',
            fields=[
                ('idgasto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=500, null=True)),
                ('tipo', models.CharField(blank=True, max_length=500, null=True)),
                ('idcategasto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Categasto')),
            ],
            options={
                'db_table': 'gastos',
            },
        ),
        migrations.CreateModel(
            name='Grp',
            fields=[
                ('idgrp', models.AutoField(db_column='IdGrp', primary_key=True, serialize=False)),
                ('cgrp', models.CharField(blank=True, db_column='cGrp', max_length=20, null=True)),
            ],
            options={
                'db_table': 'grp',
            },
        ),
        migrations.CreateModel(
            name='Grpusr',
            fields=[
                ('idgrpusr', models.AutoField(db_column='IdGrpUsr', primary_key=True, serialize=False)),
                ('idgrp', models.IntegerField(db_column='IdGrp')),
                ('idusr', models.CharField(db_column='IdUsr', max_length=15)),
            ],
            options={
                'db_table': 'grpusr',
            },
        ),
        migrations.CreateModel(
            name='Ingresos',
            fields=[
                ('idingreso', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=500, null=True)),
                ('tipo', models.CharField(blank=True, max_length=500, null=True)),
                ('idcateingreso', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ingresos',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('idopc', models.AutoField(db_column='IdOpc', primary_key=True, serialize=False)),
                ('cnomopc', models.CharField(blank=True, db_column='cNomOpc', max_length=20, null=True)),
                ('nidbar', models.IntegerField(blank=True, db_column='nIdBar', null=True)),
                ('caccion', models.CharField(blank=True, db_column='cAccion', max_length=50, null=True)),
                ('cdescripcion', models.CharField(blank=True, db_column='cDescripcion', max_length=50, null=True)),
            ],
            options={
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('idmovimiento', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=50, null=True)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('hora', models.TimeField(blank=True, null=True)),
                ('usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('saldo', models.IntegerField(blank=True, null=True)),
                ('idbodega', models.IntegerField(blank=True, null=True)),
                ('idcompra', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movimiento',
            },
        ),
        migrations.CreateModel(
            name='Municipios',
            fields=[
                ('id_municipio', models.AutoField(primary_key=True, serialize=False)),
                ('municipio', models.CharField(blank=True, max_length=50, null=True)),
                ('cod_departamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Departamentos')),
            ],
            options={
                'db_table': 'municipios',
            },
        ),
        migrations.CreateModel(
            name='Ncredito',
            fields=[
                ('codncredito', models.AutoField(primary_key=True, serialize=False)),
                ('numfacturac', models.IntegerField(blank=True, null=True)),
                ('tipo', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('sumas', models.FloatField(blank=True, null=True)),
                ('descuento', models.FloatField(blank=True, null=True)),
                ('iva', models.FloatField(blank=True, null=True)),
                ('nosujeta', models.FloatField(blank=True, null=True)),
                ('exentas', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('formadepago', models.CharField(blank=True, max_length=50, null=True)),
                ('unoretencion', models.FloatField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('tiraje', models.CharField(blank=True, max_length=50, null=True)),
                ('fechalimite', models.DateField(blank=True, null=True)),
                ('etilico', models.FloatField(blank=True, null=True)),
                ('advalorem', models.FloatField(blank=True, null=True)),
                ('especifico', models.FloatField(blank=True, null=True)),
                ('bonificacion', models.FloatField(blank=True, null=True)),
                ('descuento1', models.FloatField(blank=True, null=True)),
                ('codfacturac', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Facturacompra')),
            ],
            options={
                'db_table': 'ncredito',
            },
        ),
        migrations.CreateModel(
            name='Notacredito',
            fields=[
                ('idnotacredito', models.AutoField(primary_key=True, serialize=False)),
                ('numfacturac', models.IntegerField(blank=True, null=True)),
                ('tipo', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('sumas', models.FloatField(blank=True, null=True)),
                ('descuento', models.FloatField(blank=True, null=True)),
                ('iva', models.FloatField(blank=True, null=True)),
                ('nosujeta', models.FloatField(blank=True, null=True)),
                ('exentas', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('formadepago', models.CharField(blank=True, max_length=50, null=True)),
                ('unoretencion', models.FloatField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('tiraje', models.CharField(blank=True, max_length=50, null=True)),
                ('fechalimite', models.DateField(blank=True, null=True)),
                ('etilico', models.FloatField(blank=True, null=True)),
                ('advalorem', models.FloatField(blank=True, null=True)),
                ('especifico', models.FloatField(blank=True, null=True)),
                ('bonificacion', models.FloatField(blank=True, null=True)),
                ('descuento1', models.FloatField(blank=True, null=True)),
                ('codfacturac', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Facturacompra')),
            ],
            options={
                'db_table': 'notacredito',
            },
        ),
        migrations.CreateModel(
            name='Notificaciones',
            fields=[
                ('idnoti', models.AutoField(primary_key=True, serialize=False)),
                ('orden', models.IntegerField(blank=True, null=True)),
                ('tipo', models.CharField(blank=True, max_length=50, null=True)),
                ('cliente', models.CharField(blank=True, max_length=50, null=True)),
                ('cantidad', models.FloatField(blank=True, null=True)),
                ('idfacturav', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Facturaventa')),
            ],
            options={
                'db_table': 'notificaciones',
            },
        ),
        migrations.CreateModel(
            name='Numeros',
            fields=[
                ('idnumeros', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('nombre', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'numeros',
            },
        ),
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('idpermiso', models.AutoField(db_column='IdPermiso', primary_key=True, serialize=False)),
                ('idgrp', models.IntegerField(db_column='IdGrp')),
                ('idopc', models.IntegerField(db_column='IdOpc')),
            ],
            options={
                'db_table': 'permisos',
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codproducto', models.CharField(max_length=500)),
                ('nombre', models.CharField(blank=True, max_length=500, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=500, null=True)),
                ('precio_unit', models.FloatField(blank=True, null=True)),
                ('precioindi', models.FloatField(blank=True, null=True)),
                ('preciopublico', models.FloatField(blank=True, null=True)),
                ('existencias', models.FloatField(blank=True, null=True)),
                ('id_categoria', models.IntegerField(blank=True, null=True)),
                ('unid_med', models.CharField(blank=True, max_length=50, null=True)),
                ('valida', models.CharField(blank=True, max_length=50, null=True)),
                ('popular', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('frecuente', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('mayoreo', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
            ],
            options={
                'db_table': 'productos',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('codproveedor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=250, null=True)),
                ('nit', models.CharField(blank=True, max_length=250, null=True)),
                ('nrc', models.CharField(blank=True, max_length=250, null=True)),
                ('giro', models.CharField(blank=True, max_length=250, null=True)),
                ('direccion', models.CharField(blank=True, max_length=250, null=True)),
                ('telefono', models.CharField(blank=True, max_length=250, null=True)),
                ('fax', models.CharField(blank=True, max_length=250, null=True)),
                ('e_mail', models.CharField(blank=True, max_length=250, null=True)),
                ('estado', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'proveedor',
            },
        ),
        migrations.CreateModel(
            name='Respaldos',
            fields=[
                ('idrespaldo', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.CharField(blank=True, max_length=200, null=True)),
                ('nombrearchivo', models.CharField(blank=True, max_length=150, null=True)),
                ('automatico', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'respaldos',
            },
        ),
        migrations.CreateModel(
            name='Tablaprecios',
            fields=[
                ('idtablaprecios', models.AutoField(primary_key=True, serialize=False)),
                ('precio1', models.FloatField(blank=True, null=True)),
                ('precio2', models.FloatField(blank=True, null=True)),
                ('precio3', models.FloatField(blank=True, null=True)),
                ('codcliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Cliente')),
                ('codproducto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Productos')),
            ],
            options={
                'db_table': 'tablaprecios',
            },
        ),
        migrations.CreateModel(
            name='Tirajes',
            fields=[
                ('idtiraje', models.IntegerField(primary_key=True, serialize=False)),
                ('tirajefs', models.CharField(blank=True, max_length=50, null=True)),
                ('tirajefd', models.CharField(blank=True, max_length=50, null=True)),
                ('tirajefh', models.CharField(blank=True, max_length=50, null=True)),
                ('tirajefa', models.CharField(blank=True, max_length=50, null=True)),
                ('tirajecs', models.CharField(blank=True, max_length=50, null=True)),
                ('tirajecd', models.CharField(blank=True, max_length=50, null=True)),
                ('tirajech', models.CharField(blank=True, max_length=50, null=True)),
                ('tirajeca', models.CharField(blank=True, max_length=50, null=True)),
                ('tirajesimple', models.CharField(blank=True, max_length=500, null=True)),
                ('corrsimple', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tirajes',
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('idturno', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('numeroturno', models.IntegerField(blank=True, null=True)),
                ('fechaini', models.DateField(blank=True, null=True)),
                ('horaini', models.TimeField(blank=True, null=True)),
                ('fechafinal', models.DateField(blank=True, null=True)),
                ('horafinal', models.TimeField(blank=True, null=True)),
                ('turnoanterior', models.FloatField(blank=True, null=True)),
                ('desde', models.IntegerField(blank=True, null=True)),
                ('hasta', models.IntegerField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('activo', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'turno',
            },
        ),
        migrations.CreateModel(
            name='Usr',
            fields=[
                ('idusr', models.CharField(db_column='IdUsr', max_length=15, primary_key=True, serialize=False)),
                ('cnom', models.CharField(blank=True, db_column='cNom', max_length=20, null=True)),
                ('cape', models.CharField(blank=True, db_column='cApe', max_length=20, null=True)),
                ('cclave', models.CharField(blank=True, db_column='cClave', max_length=80, null=True)),
                ('cestado', models.CharField(blank=True, db_column='cEstado', max_length=2, null=True)),
            ],
            options={
                'db_table': 'usr',
            },
        ),
        migrations.AddField(
            model_name='notacredito',
            name='codproveedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Proveedor'),
        ),
        migrations.AddField(
            model_name='ncredito',
            name='codproveedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Proveedor'),
        ),
        migrations.AddField(
            model_name='facturacompra',
            name='codproveedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Proveedor'),
        ),
        migrations.AddField(
            model_name='dtncredito',
            name='codncredito',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Ncredito'),
        ),
        migrations.AddField(
            model_name='dtncredito',
            name='codproducto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Productos'),
        ),
        migrations.AddField(
            model_name='direccion',
            name='id_municipio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Municipios'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='codfacturav',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Facturaventa'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='codproducto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Productos'),
        ),
        migrations.AddField(
            model_name='detallenotacredito',
            name='codnotacredito',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Notacredito'),
        ),
        migrations.AddField(
            model_name='detallenotacredito',
            name='codproducto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Productos'),
        ),
        migrations.AddField(
            model_name='detalleingreso',
            name='idingreso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Ingresos'),
        ),
        migrations.AddField(
            model_name='detallegasto',
            name='idgasto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Gastos'),
        ),
        migrations.AddField(
            model_name='detalledia',
            name='iddia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Dia'),
        ),
        migrations.AddField(
            model_name='detallecreditos',
            name='codproducto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Productos'),
        ),
        migrations.AddField(
            model_name='detallecompra',
            name='codfacturac',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.Facturacompra'),
        ),
        migrations.AddField(
            model_name='detallecompra',
            name='codproducto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Productos'),
        ),
        migrations.AddField(
            model_name='bodega',
            name='idproducto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Productos'),
        ),
    ]