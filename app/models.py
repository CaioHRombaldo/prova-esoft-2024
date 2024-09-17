from django.db import models
from django.urls import reverse


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Curso(BaseModel):
    nome = models.CharField('Nome', max_length=100)
    cargaHoraria = models.IntegerField()
    dataInicio = models.DateField()

    def addDisciplina(self, item):
        item.curso = self
        item.save()

    def removeDisciplina(self, item):
        item.curso = None
        item.save()

    def __str__(self) -> str:
        return f'{self.nome}'
    
    def get_absolute_url(self):
        return reverse("curso-detail", kwargs={"pk": self.pk})
        
class Disciplina(BaseModel):
    nome = models.CharField('Nome', max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        if self.curso:
            return f'{self.nome} - {self.curso}'
        
        return f'{self.nome}'
        