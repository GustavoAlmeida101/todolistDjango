from django.db import models


class lista(models.Model):
    tarefa = models.CharField(max_length=100)
    dia = models.DateTimeField()
    
    def __str__(self):
       return self.tarefa
   
     
    
