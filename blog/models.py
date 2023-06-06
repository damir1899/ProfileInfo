from django.db import models


STATUS_CHOICES = (
    ('Ментор', 'Ментор'),
    ('Студент', 'Студент'),
    ('Работник', 'Работник'),
    ('Не указано', 'Не указано'),
)

GENDER_CHOICES = (
    ('Женский', 'Женский'),
    ('Мужской', 'Мужской'),
    ('Другой', 'Другой'),
    ('Не указано', 'Не указано')
)

class Profile(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    email = models.EmailField(verbose_name='Электроння почта')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')
    image = models.ImageField(upload_to='profile_image/', verbose_name='Фотография профиля')
    status = models.CharField(max_length=20, verbose_name='Статус', choices=STATUS_CHOICES, default='Не указано')
    gender = models.CharField(max_length=50, verbose_name='Пол', choices=GENDER_CHOICES, default='Не указано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистраций')
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
    