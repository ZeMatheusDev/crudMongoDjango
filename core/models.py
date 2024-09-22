from django.db import models

class Usuario(models.Model):
    email = models.CharField(max_length=500)
    login = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    token = models.CharField(max_length=100)

    class Meta:
        db_table = 'usuarios' 
