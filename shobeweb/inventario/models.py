# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return str(self.nombre)    

class Productos(models.Model):
    codproducto = models.CharField(primary_key=True,max_length=255)
    nombre = models.CharField(max_length=500, blank=True, null=True)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    precio_unit = models.FloatField(blank=True, null=True)
    precioindi = models.FloatField(blank=True, null=True)
    preciopublico = models.FloatField(blank=True, null=True)
    existencias = models.FloatField(blank=True, null=True)
    id_categoria = models.IntegerField(blank=True, null=True)
    unid_med = models.CharField(max_length=50, blank=True, null=True)
    valida = models.CharField(max_length=50, blank=True, null=True)
    popular = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    frecuente = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    mayoreo = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'productos'

    def __str__(self):
        return str(self.nombre) 


class Cajas(models.Model):
    idcajas = models.AutoField(primary_key=True)
    cajachica = models.FloatField(blank=True, null=True)
    cajagrande = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'cajas'


class Categasto(models.Model):
    idcategasto = models.AutoField(primary_key=True)
    gasto = models.CharField(max_length=500, blank=True, null=True)
    tipo = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'categasto'





class Cateingreso(models.Model):
    idcateingreso = models.AutoField(primary_key=True)
    ingreso = models.CharField(max_length=500, blank=True, null=True)
    tipo = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'cateingreso'


class Cliente(models.Model):
    codcliente_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250, blank=True, null=True)
    nit = models.CharField(max_length=250, blank=True, null=True)
    nrc = models.CharField(max_length=250, blank=True, null=True)
    giro = models.CharField(max_length=250, blank=True, null=True)
    direccion = models.CharField(max_length=250, blank=True, null=True)
    telefono = models.CharField(max_length=250, blank=True, null=True)
    fax = models.CharField(max_length=250, blank=True, null=True)
    e_mail = models.CharField(max_length=250, blank=True, null=True)
    estado = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'cliente'
    
    def __str__(self):
        return str(self.nombre)  
    
  


class Clientes(models.Model):
    idclientes = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'clientes'


class Configuraciones(models.Model):
    id_config = models.AutoField(primary_key=True)
    tirage_fact = models.CharField(max_length=250, blank=True, null=True)
    tirage_compro = models.CharField(max_length=250, blank=True, null=True)
    tirage_fact_actual = models.CharField(max_length=250, blank=True, null=True)
    tirage_compro_actual = models.CharField(max_length=250, blank=True, null=True)
    numfact = models.CharField(max_length=250, blank=True, null=True)
    numcompro = models.CharField(max_length=250, blank=True, null=True)
    iva = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    cotrans = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    porce_iva_ret = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)

    class Meta:
        db_table = 'configuraciones'


class Proveedor(models.Model):
    codproveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250, blank=True, null=True)
    nit = models.CharField(max_length=250, blank=True, null=True)
    nrc = models.CharField(max_length=250, blank=True, null=True)
    giro = models.CharField(max_length=250, blank=True, null=True)
    direccion = models.CharField(max_length=250, blank=True, null=True)
    telefono = models.CharField(max_length=250, blank=True, null=True)
    fax = models.CharField(max_length=250, blank=True, null=True)
    e_mail = models.CharField(max_length=250, blank=True, null=True)
    estado = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'proveedor'
    
    


class Facturacompra(models.Model):
    codfacturac = models.AutoField(primary_key=True)
    numfacturac = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    codproveedor = models.IntegerField(null=True,blank=True) 
    fecha = models.DateField(blank=True, null=True)
    sumas = models.FloatField(blank=True, null=True)
    descuento = models.FloatField(blank=True, null=True)
    iva = models.FloatField(blank=True, null=True)
    nosujeta = models.FloatField(blank=True, null=True)
    exentas = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    formadepago = models.CharField(max_length=50, blank=True, null=True)
    unoretencion = models.FloatField(blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    tiraje = models.CharField(max_length=50, blank=True, null=True)
    fechalimite = models.DateField(blank=True, null=True)
    etilico = models.FloatField(blank=True, null=True)
    advalorem = models.FloatField(blank=True, null=True)
    especifico = models.FloatField(blank=True, null=True)
    bonificacion = models.FloatField(blank=True, null=True)
    descuento1 = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'facturacompra'

    


class Facturaventa(models.Model):
    codfacturav = models.AutoField(primary_key=True)
    numfacturav = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    codcliente = models.IntegerField(null=True,blank=True) 
    fecha = models.DateTimeField(blank=True, null=True)
    sumas = models.FloatField(blank=True, null=True)
    descuento = models.FloatField(blank=True, null=True)
    iva = models.FloatField(blank=True, null=True)
    nosujeta = models.FloatField(blank=True, null=True)
    exentas = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    formadepago = models.CharField(max_length=50, blank=True, null=True)
    unoretencion = models.FloatField(blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    tiraje = models.CharField(max_length=50, blank=True, null=True)
    fechavence = models.DateTimeField(blank=True, null=True)
    comision = models.FloatField(blank=True, null=True)
    generada = models.IntegerField(blank=True, null=True)
    efectivo = models.FloatField(blank=True, null=True)
    cambio = models.FloatField(blank=True, null=True)
    usuario = models.CharField(max_length=50, blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    turno = models.IntegerField(blank=True, null=True)
    dia = models.IntegerField(blank=True, null=True)

    class Meta: 
        db_table = 'facturaventa'


class Creditos(models.Model):
    idcredito = models.AutoField(primary_key=True)
    monto = models.FloatField(blank=True, null=True)
    totalproducto = models.FloatField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    idclientes = models.IntegerField(null=True,blank=True)

    class Meta:
        db_table = 'creditos'


class Departamentos(models.Model):
    cod_departamento = models.AutoField(primary_key=True)
    departamentos = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'departamentos'


class Detallecompra(models.Model):
    coddetallefacturac = models.AutoField(primary_key=True)
    codfacturac = models.IntegerField(blank=True, null=True)
    codfacturac = models.IntegerField(null=True,blank=True) 
    codproducto = models.IntegerField(null=True,blank=True) 
    cantidadunit = models.FloatField(blank=True, null=True)
    descuento = models.FloatField(blank=True, null=True)
    precioreal = models.FloatField(blank=True, null=True)
    preciodescuento = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    total1 = models.FloatField(blank=True, null=True)
    preciopublico = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'detallecompra'


class Detallecreditos(models.Model):
    iddetallecreditos = models.AutoField(primary_key=True)
    idcredito = models.IntegerField(blank=True, null=True)
    codproducto = models.IntegerField(null=True,blank=True) 
    precio = models.FloatField(blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'detallecreditos'

class Dia(models.Model):
    iddia = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50, blank=True, null=True)
    numdia = models.IntegerField(blank=True, null=True)
    fechaini = models.DateField(blank=True, null=True)
    horaini = models.TimeField(blank=True, null=True)
    fechafinal = models.DateField(blank=True, null=True)
    horafinal = models.TimeField(blank=True, null=True)
    dianterior = models.FloatField(blank=True, null=True)
    desde = models.IntegerField(blank=True, null=True)
    hasta = models.IntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    activo = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'dia'


class Detalledia(models.Model):
    iddetalledia = models.AutoField(primary_key=True)
    iddia = models.IntegerField(null=True,blank=True) 
    idturno = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'detalledia'


class Gastos(models.Model):
    idgasto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=500, blank=True, null=True)
    tipo = models.CharField(max_length=500, blank=True, null=True)
    idcategasto = models.IntegerField(null=True,blank=True) 

    class Meta:
        db_table = 'gastos'


class Detallegasto(models.Model):
    iddetallegasto = models.AutoField(primary_key=True)
    idgasto = models.IntegerField(null=True,blank=True) 
    cantidad = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    razon = models.CharField(max_length=500, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'detallegasto'

class Ingresos(models.Model):
    idingreso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=500, blank=True, null=True)
    tipo = models.CharField(max_length=500, blank=True, null=True)
    idcateingreso = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ingresos'

class Detalleingreso(models.Model):
    iddetalleingreso = models.AutoField(primary_key=True)
    idingreso = models.IntegerField(null=True,blank=True) 
    cantidad = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    razon = models.CharField(max_length=500, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'detalleingreso'



class Ncredito(models.Model):
    codncredito = models.AutoField(primary_key=True)
    numfacturac = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    codproveedor = models.IntegerField(null=True,blank=True) 
    fecha = models.DateField(blank=True, null=True)
    sumas = models.FloatField(blank=True, null=True)
    descuento = models.FloatField(blank=True, null=True)
    iva = models.FloatField(blank=True, null=True)
    nosujeta = models.FloatField(blank=True, null=True)
    exentas = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    formadepago = models.CharField(max_length=50, blank=True, null=True)
    unoretencion = models.FloatField(blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    tiraje = models.CharField(max_length=50, blank=True, null=True)
    fechalimite = models.DateField(blank=True, null=True)
    etilico = models.FloatField(blank=True, null=True)
    advalorem = models.FloatField(blank=True, null=True)
    especifico = models.FloatField(blank=True, null=True)
    bonificacion = models.FloatField(blank=True, null=True)
    descuento1 = models.FloatField(blank=True, null=True)
    codfacturac = models.IntegerField(null=True,blank=True) 

    class Meta:
        db_table = 'ncredito'


class Notacredito(models.Model):
    idnotacredito = models.AutoField(primary_key=True)
    numfacturac = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    codproveedor = models.IntegerField(null=True,blank=True) 
    fecha = models.DateField(blank=True, null=True)
    sumas = models.FloatField(blank=True, null=True)
    descuento = models.FloatField(blank=True, null=True)
    iva = models.FloatField(blank=True, null=True)
    nosujeta = models.FloatField(blank=True, null=True)
    exentas = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    formadepago = models.CharField(max_length=50, blank=True, null=True)
    unoretencion = models.FloatField(blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    tiraje = models.CharField(max_length=50, blank=True, null=True)
    fechalimite = models.DateField(blank=True, null=True)
    etilico = models.FloatField(blank=True, null=True)
    advalorem = models.FloatField(blank=True, null=True)
    especifico = models.FloatField(blank=True, null=True)
    bonificacion = models.FloatField(blank=True, null=True)
    descuento1 = models.FloatField(blank=True, null=True)
    codfacturac = models.IntegerField(null=True,blank=True) 

    class Meta:
        db_table = 'notacredito'



class Detallenotacredito(models.Model):
    coddetallenotacredito = models.AutoField(primary_key=True)
    codnotacredito = models.IntegerField(null=True,blank=True) 
    codproducto = models.IntegerField(null=True,blank=True) 
    cantidadunit = models.FloatField(blank=True, null=True)
    descuento = models.FloatField(blank=True, null=True)
    precioreal = models.FloatField(blank=True, null=True)
    preciodescuento = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    total1 = models.FloatField(blank=True, null=True)
    preciopublico = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'detallenotacredito'


class Detalleventa(models.Model):
    coddetallefacturav = models.AutoField(primary_key=True)
    codfacturav = models.IntegerField(null=True,blank=True) 
    codproducto = models.IntegerField(null=True,blank=True) 
    cantidadunit = models.FloatField(blank=True, null=True)
    descuento = models.FloatField(blank=True, null=True)
    precioreal = models.FloatField(blank=True, null=True)
    preciodescuento = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    total1 = models.FloatField(blank=True, null=True)
    preciopublico = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'detalleventa'


class Municipios(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    municipio = models.CharField(max_length=50, blank=True, null=True)
    cod_departamento = models.IntegerField(null=True,blank=True) 
    

    class Meta:
        db_table = 'municipios'


class Direccion(models.Model):
    id_direcciones = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=1000, blank=True, null=True)
    id_municipio = models.IntegerField(null=True,blank=True) 
    
    class Meta:
        db_table = 'direccion'






class Dtncredito(models.Model):
    coddtncredito = models.AutoField(primary_key=True)
    codncredito = models.IntegerField(null=True,blank=True) 
    codproducto = models.IntegerField(null=True,blank=True) 
    cantidadunit = models.FloatField(blank=True, null=True)
    descuento = models.FloatField(blank=True, null=True)
    precioreal = models.FloatField(blank=True, null=True)
    preciodescuento = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    total1 = models.FloatField(blank=True, null=True)
    preciopublico = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'dtncredito'





class Fechaabono(models.Model):
    idfecha = models.AutoField(primary_key=True)
    iddoc = models.IntegerField(blank=True, null=True)
    fechaabono = models.DateTimeField(blank=True, null=True)
    cantidadabono = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'fechaabono'





class Grp(models.Model):
    idgrp = models.AutoField(db_column='IdGrp', primary_key=True)  # Field name made lowercase.
    cgrp = models.CharField(db_column='cGrp', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'grp'


class Grpusr(models.Model):
    idgrpusr = models.AutoField(db_column='IdGrpUsr', primary_key=True)  # Field name made lowercase.
    idgrp = models.IntegerField(db_column='IdGrp')  # Field name made lowercase.
    idusr = models.CharField(db_column='IdUsr', max_length=15)  # Field name made lowercase.

    class Meta:
        db_table = 'grpusr'





class Menu(models.Model):
    idopc = models.AutoField(db_column='IdOpc', primary_key=True)  # Field name made lowercase.
    cnomopc = models.CharField(db_column='cNomOpc', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nidbar = models.IntegerField(db_column='nIdBar', blank=True, null=True)  # Field name made lowercase.
    caccion = models.CharField(db_column='cAccion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cdescripcion = models.CharField(db_column='cDescripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'menu'


class Movimiento(models.Model):
    idmovimiento = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    usuario = models.CharField(max_length=50, blank=True, null=True)
    saldo = models.IntegerField(blank=True, null=True)
    idbodega = models.IntegerField(blank=True, null=True)
    idcompra = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'movimiento'





class Notificaciones(models.Model):
    idnoti = models.AutoField(primary_key=True)
    orden = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    cliente = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    idfacturav = models.IntegerField(null=True,blank=True) 

    class Meta:
        db_table = 'notificaciones'


class Numeros(models.Model):
    idnumeros = models.AutoField(primary_key=True)
    numero = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        db_table = 'numeros'


class Permisos(models.Model):
    idpermiso = models.AutoField(db_column='IdPermiso', primary_key=True)  # Field name made lowercase.
    idgrp = models.IntegerField(db_column='IdGrp')  # Field name made lowercase.
    idopc = models.IntegerField(db_column='IdOpc')  # Field name made lowercase.

    class Meta:
        db_table = 'permisos'






class Respaldos(models.Model):
    idrespaldo = models.AutoField(primary_key=True)
    fecha = models.CharField(max_length=200, blank=True, null=True)
    nombrearchivo = models.CharField(max_length=150, blank=True, null=True)
    automatico = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        db_table = 'respaldos'


class Tablaprecios(models.Model):
    idtablaprecios = models.AutoField(primary_key=True)
    codcliente = models.IntegerField(null=True,blank=True) 
    codproducto = models.IntegerField(null=True,blank=True) 
    precio1 = models.FloatField(blank=True, null=True)
    precio2 = models.FloatField(blank=True, null=True)
    precio3 = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'tablaprecios'


class Tirajes(models.Model):
    idtiraje = models.IntegerField(primary_key=True)
    tirajefs = models.CharField(max_length=50, blank=True, null=True)
    tirajefd = models.CharField(max_length=50, blank=True, null=True)
    tirajefh = models.CharField(max_length=50, blank=True, null=True)
    tirajefa = models.CharField(max_length=50, blank=True, null=True)
    tirajecs = models.CharField(max_length=50, blank=True, null=True)
    tirajecd = models.CharField(max_length=50, blank=True, null=True)
    tirajech = models.CharField(max_length=50, blank=True, null=True)
    tirajeca = models.CharField(max_length=50, blank=True, null=True)
    tirajesimple = models.CharField(max_length=500, blank=True, null=True)
    corrsimple = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'tirajes'


class Turno(models.Model):
    idturno = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50, blank=True, null=True)
    numeroturno = models.IntegerField(blank=True, null=True)
    fechaini = models.DateField(blank=True, null=True)
    horaini = models.TimeField(blank=True, null=True)
    fechafinal = models.DateField(blank=True, null=True)
    horafinal = models.TimeField(blank=True, null=True)
    turnoanterior = models.FloatField(blank=True, null=True)
    desde = models.IntegerField(blank=True, null=True)
    hasta = models.IntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    activo = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'turno'


class Usr(models.Model):
    idusr = models.CharField(db_column='IdUsr', primary_key=True, max_length=15)  # Field name made lowercase.
    cnom = models.CharField(db_column='cNom', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cape = models.CharField(db_column='cApe', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cclave = models.CharField(db_column='cClave', max_length=80, blank=True, null=True)  # Field name made lowercase.
    cestado = models.CharField(db_column='cEstado', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'usr'
