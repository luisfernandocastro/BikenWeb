# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
    


class Bicicletas(models.Model):
    idbicicletas = models.AutoField(db_column='idBicicletas', primary_key=True)  # Field name made lowercase.
    marca = models.CharField(db_column='Marca', max_length=45)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=50)  # Field name made lowercase.
    material = models.TextField(db_column='Material')  # Field name made lowercase.
    categoria = models.ForeignKey('Categoria', models.DO_NOTHING, db_column='Categoria')  # Field name made lowercase.
    precioalquiler = models.DecimalField(db_column='PrecioAlquiler', max_digits=6, decimal_places=3,verbose_name='Precio Alquiler')  # Field name made lowercase.
    foto = models.ImageField(db_column='Foto', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bicicletas'
        verbose_name_plural='Bicicleta' 

    def __str__(self):
        return self.marca

class Catalogo(models.Model):
    idcatalogo = models.AutoField(db_column='idCatalogo', primary_key=True)  # Field name made lowercase.
    bicicleta = models.ForeignKey(Bicicletas, models.DO_NOTHING, db_column='Bicicleta')  # Field name made lowercase.
    fechahorasubida = models.DateTimeField(db_column='fechaHoraSubida')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'catalogo'
        verbose_name_plural='Catalogo' 

class Categoria(models.Model):
    idmodelo = models.AutoField(db_column='idModelo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categoria'
        verbose_name_plural='Categoria' 


    def __str__(self):
        return self.nombre


class Contrato(models.Model):
    idcontrato = models.AutoField(db_column='idContrato', primary_key=True)  # Field name made lowercase.
    cantidadbicicletas = models.IntegerField(db_column='CantidadBicicletas')  # Field name made lowercase.
    fechainicio = models.DateField(db_column='FechaInicio')  # Field name made lowercase.
    fechafin = models.DateField(db_column='FechaFin')  # Field name made lowercase.
    tiempo = models.TimeField(db_column='Tiempo')  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=100)  # Field name made lowercase.
    tipocontrato = models.ForeignKey('Tipocontrato', models.DO_NOTHING, db_column='Tipocontrato')  # Field name made lowercase.
    persona_idpersona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='Persona_idPersona')  # Field name made lowercase.
    bicicletas_idbicicletas = models.ForeignKey(Bicicletas, models.DO_NOTHING, db_column='Bicicletas_idBicicletas')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contrato'
        verbose_name_plural='Contrato'

class FotoPerfiluser(models.Model):
    idfotouser = models.AutoField(db_column='idfotoUser', primary_key=True)  # Field name made lowercase.
    foto = models.ImageField(max_length=100)
    usuario_idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario_idUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'foto_perfiluser'
        verbose_name_plural='Foto perfil Usuario'


class Modulo(models.Model):
    idmodulo = models.AutoField(db_column='idModulo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'modulo'


class Pagos(models.Model):
    idpago = models.AutoField(db_column='idPago', primary_key=True)  # Field name made lowercase.
    fechapago = models.DateTimeField(db_column='FechaPago')  # Field name made lowercase.
    totalalquiler = models.DecimalField(db_column='TotalAlquiler', max_digits=6, decimal_places=3)  # Field name made lowercase.
    fechamora = models.DateTimeField(db_column='FechaMora', blank=True, null=True)  # Field name made lowercase.
    contrato = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='Contrato')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pagos'
        verbose_name_plural='Pagos' 

    def __str__(self):
        return self.totalalquiler


class Perfilusuario(models.Model):
    idroles = models.AutoField(db_column='idRoles', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    descripcionrol = models.TextField(db_column='descripcionRol', blank=True, null=True)  # Field name made lowercase.
    usuario_idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario_idUsuario')  # Field name made lowercase.
    modulo_idmodulo = models.ForeignKey(Modulo, models.DO_NOTHING, db_column='Modulo_idModulo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'perfilusuario'
        verbose_name_plural='Perfil Usuario' 


class Persona(models.Model):
    idpersona = models.AutoField(db_column='idPersona', primary_key=True)  # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=50)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=50)  # Field name made lowercase.
    numidentificacion = models.BigIntegerField(db_column='NumIdentificacion',verbose_name='Num Identificaci??n')  # Field name made lowercase.
    numcelular = models.BigIntegerField(db_column='NumCelular',verbose_name='Num Celular')  # Field name made lowercase.
    numtelefono = models.BigIntegerField(db_column='NumTelefono', blank=True, null=True,verbose_name='Num T??lefono')  # Field name made lowercase.
    correoelectronico = models.CharField(db_column='CorreoElectronico', max_length=45,verbose_name='Correo Electr??nico')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'persona'
        verbose_name_plural='Persona' 


    def __str__(self):
        cadenaName = self.nombres + ' ' + self.apellidos
        return cadenaName


class Privilegios(models.Model):
    idprivilegios = models.AutoField(db_column='idPrivilegios', primary_key=True)  # Field name made lowercase.
    privilegio = models.IntegerField()
    modulo_idmodulo = models.ForeignKey(Modulo, models.DO_NOTHING, db_column='Modulo_idModulo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'privilegios'


class Reserva(models.Model):
    idreserva = models.AutoField(db_column='idReserva', primary_key=True)  # Field name made lowercase.
    bicicleta = models.ForeignKey(Bicicletas, models.DO_NOTHING, db_column='Bicicleta')  # Field name made lowercase.
    disponibleen = models.TimeField(db_column='DisponibleEn', blank=True, null=True)  # Field name made lowercase.
    disponible = models.CharField(db_column='Disponible', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reserva'
        verbose_name_plural='Reserva' 


class Tiempoprestamo(models.Model):
    idtiempodisponibilidad = models.IntegerField(db_column='idTiempoDisponibilidad', primary_key=True)  # Field name made lowercase.
    bicicletas_idbicicletas = models.ForeignKey(Bicicletas, models.DO_NOTHING, db_column='Bicicletas_idBicicletas')  # Field name made lowercase.
    contrato_idcontrato = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='Contrato_idContrato')  # Field name made lowercase.
    tiempoinicio = models.CharField(db_column='tiempoInicio', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tiempoprestamo'
        verbose_name_plural='Tiempo Prestamo'


class Tipocontrato(models.Model):
    idtipocontrato = models.IntegerField(db_column='idTipocontrato', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipocontrato'


class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=20)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100)  # Field name made lowercase.
    persona_idpersona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='Persona_idPersona')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'



