from django.db import models

# Create your models here.
class InternetNauta(models.Model):
    nauta_username = models.CharField(max_length=500)
    nauta_password = models.CharField(max_length=500)
    connected = models.BooleanField(default=False)

    def __str__(self):
        return "Internet Nauta"

    class Meta:
        verbose_name = "Internet Nauta"
        verbose_name_plural = "Internet Nauta"

class QrData(models.Model):
    uri = models.CharField(max_length=500)

    def __str__(self):
        return "QR"

    class Meta:
        verbose_name = "QR"
        verbose_name_plural = "QR"