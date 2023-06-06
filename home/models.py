from django.db import models


class Contact(models.Model):
    image = models.ImageField(upload_to='contact/', verbose_name='Изображение')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    phone = models.CharField(max_length=12, verbose_name='Номер')
    email = models.EmailField(max_length=120, verbose_name='Электронная почта')
    
    
    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
