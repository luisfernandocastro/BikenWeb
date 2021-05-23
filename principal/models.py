# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bicicletas(models.Model):
    idbicicletas = models.AutoField(db_column='idBicicletas', primary_key=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=50)  # Field name made lowercase.
    material = models.TextField(db_column='Material')  # Field name made lowercase.
    categoria = models.ForeignKey('Categoria', models.DO_NOTHING, db_column='Categoria')  # Field name made lowercase.
    precioalquiler = models.DecimalField(db_column='PrecioAlquiler', max_digits=6, decimal_places=3)  # Field name made lowercase.
    foto = models.CharField(db_column='Foto', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bicicletas'


class Catalogo(models.Model):
    idcatalogo = models.AutoField(db_column='idCatalogo', primary_key=True)  # Field name made lowercase.
    bicicleta = models.ForeignKey(Bicicletas, models.DO_NOTHING, db_column='Bicicleta')  # Field name made lowercase.
    fechahorasubida = models.DateTimeField(db_column='fechaHoraSubida')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'catalogo'


class Categoria(models.Model):
    idmodelo = models.AutoField(db_column='idModelo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categoria'


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class Perfilusuario(models.Model):
    idroles = models.AutoField(db_column='idRoles', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    descripcionrol = models.TextField(db_column='descripcionRol', blank=True, null=True)  # Field name made lowercase.
    usuario_idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario_idUsuario')  # Field name made lowercase.
    modulo_idmodulo = models.ForeignKey(Modulo, models.DO_NOTHING, db_column='Modulo_idModulo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'perfilusuario'


class Persona(models.Model):
    idpersona = models.AutoField(db_column='idPersona', primary_key=True)  # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=50)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=50)  # Field name made lowercase.
    numidentificacion = models.BigIntegerField(db_column='NumIdentificacion')  # Field name made lowercase.
    numcelular = models.BigIntegerField(db_column='NumCelular')  # Field name made lowercase.
    numtelefono = models.BigIntegerField(db_column='NumTelefono', blank=True, null=True)  # Field name made lowercase.
    correoelectronico = models.CharField(db_column='CorreoElectronico', max_length=45)  # Field name made lowercase. # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'persona'


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


class Tiempoprestamo(models.Model):
    idtiempodisponibilidad = models.IntegerField(db_column='idTiempoDisponibilidad', primary_key=True)  # Field name made lowercase.
    bicicletas_idbicicletas = models.ForeignKey(Bicicletas, models.DO_NOTHING, db_column='Bicicletas_idBicicletas')  # Field name made lowercase.
    contrato_idcontrato = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='Contrato_idContrato')  # Field name made lowercase.
    tiempoinicio = models.CharField(db_column='tiempoInicio', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tiempoprestamo'


class Tipocontrato(models.Model):
    idtipocontrato = models.IntegerField(db_column='idTipocontrato', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipocontrato'


class Tipopersona(models.Model):
    idtipopersona = models.AutoField(db_column='idtipoPersona', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=55)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipopersona'


class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    persona_idpersona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='Persona_idPersona')  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=20)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'
