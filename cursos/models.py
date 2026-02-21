from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField("nombre", max_length=80, unique=True)
    descripcion = models.TextField("descripción", blank=True)

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"

    def __str__(self):
        return self.nombre
    
class Curso(models.Model):
    # relacion cursos con la tabla categoria 
    #ci = models.CharField(primary_key=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="cursos",
        verbose_name="categoría",
    )
    titulo = models.CharField("título", max_length=100)
    descripcion = models.TextField("descripción", blank=True)
    fecha_inicio = models.DateField("fecha de inicio")
    carga_horaria = models.PositiveSmallIntegerField("carga horaria", default=0)
    activo = models.BooleanField("activo", default=True)

    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"

    def __str__(self):
        return self.titulo    
