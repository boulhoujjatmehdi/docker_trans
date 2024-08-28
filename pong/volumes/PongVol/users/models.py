from django.db import models, IntegrityError
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True, default='default_name')
    last_seen = models.DateTimeField(null=True, blank=True)
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
      
    @property
    def is_online(self):
        if self.last_seen:
            return timezone.now()
        else:
            return False
    


class TokensCustom(models.Model):
    token = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    retired = models.BooleanField(default=False)


    def is_valid(self):
        if timezone.now() < self.expires_at:
            return True
        self.delete()
        return False
    
    def save(self, *args, **kwargs):    
        if self.pk is None and TokensCustom.objects.filter(user_id = self.user_id).count() >= 3:
            TokensCustom.objects.filter(user_id = self.user_id).first().delete()
        super().save(*args,**kwargs)

    @staticmethod
    def delete_expired_tokens(user):
        TokensCustom.objects.filter(expires_at__lt = timezone.now() , user_id = user).delete()
        pass

import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django_otp.models import Device
from django_otp.plugins.otp_totp.models import TOTPDevice





def create_totp_device(user):
    totp_device , created = TOTPDevice.objects.get_or_create(user=user, confirmed=False)
    if created:
        totp_device.generate_challenge()
    return totp_device



def generate_qr_code(totp_device):
    qr_url = totp_device.config_url
    qr_image = qrcode.make(qr_url)
    buffer = BytesIO()
    qr_image.save(buffer, "PNG")
    qr_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return qr_base64

import urllib.parse
from django_otp.plugins.otp_totp.models import TOTPDevice
import base64

# def generate_qr_code(user):
#     totp_device = TOTPDevice.objects.create(user=user, confirmed=False)
#     totp_device.generate_challenge()

#     issuer = 'users'
#     label = f"{issuer}:{user.username}"
#     url = f"otpauth://totp/{urllib.parse.quote(label)}?secret={totp_device.bin_key}&issuer={urllib.parse.quote(issuer)}"

#     # Generate the QR code from this URL
#     qr = qrcode.make(totp_device.config_url)
#     buffer = BytesIO()
#     qr.save(buffer, "PNG")
    
#     # Encode the QR code image to base64
#     qr_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
#     return qr_base64