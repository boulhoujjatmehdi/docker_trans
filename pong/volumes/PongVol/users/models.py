from django.db import models, IntegrityError
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True, default='default_name')
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
    


class TokensCustom(models.Model):
    token = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    retired = models.BooleanField(default=False)

    def is_valid(self):
        return timezone.now() < self.expires_at
    
    def save(self, *args, **kwargs):
        if self.pk is None and TokensCustom.objects.filter(user_id = self.user_id).count() >= 3:
            TokensCustom.objects.filter(user_id = self.user_id).first().delete()
        super().save(*args,**kwargs)
