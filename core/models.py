from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null= True)
    data_evento = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now=True)
    
    # importa a classe User do proprio django, on_delete=models.CASCADE
    # é o comportamento do django caso o user seja deletado, cascade indica
    # que todos os eventos do user deve ser deletados
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta: 
        db_table = 'evento'
        
    def __str__(self):
        return self.titulo
    
    def get_data_evento(self):
        return self.data_evento.strftime("%d/%m/%Y")
    
    
