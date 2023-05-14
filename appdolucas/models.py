from django.db import models

#Cria a classe Task que dá os detalhes dos fields criados no forms.py, como no totle que dá o max_len de 50 caracteres

class Task(models.Model):
  title = models.CharField(max_length = 50)
  description = models.TextField()
