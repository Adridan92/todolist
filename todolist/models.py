from django.db import models

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(verbose_name='Fecha de creación')
    active = models.BooleanField(default=True, verbose_name='Activo')
    last_update = models.DateTimeField(auto_now_add=True, verbose_name='Última actualización')


    class Meta:
        managed = False
        db_table = 'status'

    def __str__(self):
        return str(self.name)


class Task(models.Model):
    status = models.ForeignKey('Status', models.DO_NOTHING, db_column='status_id')
    description = models.TextField()
    title = models.TextField(max_length=255)
    
    created_at = models.DateTimeField(verbose_name='Fecha de creación')
    active = models.BooleanField(default=True, verbose_name='Activo')
    last_update = models.DateTimeField(auto_now_add=True, verbose_name='Última actualización')

    class Meta:
        managed = False
        db_table = 'task'
