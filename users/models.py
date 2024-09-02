from django.db import models

# Create your models here.
class Users(models.Model):
    '''моделька для пользователя'''
    first_name = models.CharField(max_length=200)
    last_name = models.TextField(max_length=100)

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=8)

    phone_number = models.CharField(max_length=25,null=True,blank=True)
    address = models.TextField()
    avatar = models.ImageField()

    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()

    birthdate = models.DateField()
    date_joined_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователь'
        unique_together = ('first_name', 'last_name')#уникальное комбинация
