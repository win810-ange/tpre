from django.db import models


# Create your models here.

class Signalement(models.Model):
    type = models.CharField(max_length=255)
    image = models.ImageField(upload_to='signalement_image')
    localisation = models.CharField(max_length=255)
    jour = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.image}'
    
    def delete(self):
        return super().delete()
    