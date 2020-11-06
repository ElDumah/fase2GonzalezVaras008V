from django.db import models
from ckeditor.fields import RichTextField

class ModeloBase(models.Model):
	id = models.AutoField(primary_key = True)
	estado = models.BooleanField('Estado', default = True)
	fecha_creacion = models.DateField('fecha de creacion', auto_now = False, auto_now_add = True)
	fecha_modificacion = models.DateField('fecha de modificacion',auto_now = True, auto_now_add = False)
	fecha_eliminacion = models.DateField('fecha eliminacion', auto_now = True, auto_now_add = False)


	class Meta:
		abstract = True

class Categoria(ModeloBase):
    nombre = models.CharField('Nombre de la Categoría', max_length = 100, unique = True)
    imagen_referencial = models.ImageField('Imagen Referencial',upload_to = 'categoria/')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre

class Auto(ModeloBase):
	modelo = models.CharField('modelo del auto', max_length = 150, unique = True)
	patente = models.CharField('Patente', max_length = 150, unique = True)
	descripcion = models.TextField('Descripcion')
	categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
	contenido = RichTextField()
	imagen_referencial = models.ImageField('imagen referencial', upload_to = 'imagenes/', max_length = 255)
	publicado = models.BooleanField('Publicado / no publicado', default = False)
	fecha_publicacion = models.DateField('fecha de publicacion')
	
	class Meta:
		verbose_name = 'Auto'
		verbose_name_plural = 'Autos'

	def __str__(self):
		return self.modelo

class Web(ModeloBase):
	nosotros = models.TextField('Nosotros')	
	telefono = models.CharField('Telefono', max_length = 10)
	email = models.EmailField('Correo electronico', max_length = 200)
	direccion = models.CharField('Direccion', max_length = 200)

	class Meta:
		verbose_name = 'Web'
		verbose_name_plural = 'Webs'

	def __str__(self):
		return self.nosotros

class RedesSociales(ModeloBase):
	facebook = models.URLField('Facebook')
	twitter = models.URLField('Twitter')
	instagram = models.URLField('Instagram')

	def __str__(self):
		return self.facebook

class Contacto(ModeloBase):
	nombre = models.CharField('Nombre', max_length = 100)
	apellidos = models.CharField('Apellidos', max_length = 150)
	correo = models.EmailField('Correo electronico', max_length = 200)
	asunto = models.CharField('Asunto', max_length = 100)
	mensaje = models.TextField('Mensaje')

	class Meta: 
		verbose_name = 'Contacto'
		verbose_name_plural = 'Contactos'

	def __str__(self):
		return self.asunto
