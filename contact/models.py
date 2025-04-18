from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# Depois
# category (foreign key), show (boolean), 
# picture (imagem)

# Depois
# owner (foreign key)

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria' #muda o nome que aparece

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'

class Contact(models.Model):
    class Meta:
        verbose_name = 'Contato'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True,verbose_name='Sobrenome')
    phone = models.CharField(max_length=50, verbose_name='Telefone')
    email = models.EmailField(max_length=254,blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True,verbose_name='Descrição')
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True , upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True, null=True,verbose_name='Categoria') #tome cuidado ao usar CASCADE 
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'