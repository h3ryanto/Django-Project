from django.db import models

# Create your models here.


class Profil(models.Model):
    nama = models.CharField(max_length=20)
    alamat = models.CharField(max_length=70)

    def __str__(self):
        return "{}".format(self.nama)
