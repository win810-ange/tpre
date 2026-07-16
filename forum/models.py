from django.db import models
from user.models import User

# Create your models here.

class Discussion(models.Model):
    sujet = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.sujet}'
    
class Reponse(models.Model):
    Sujet = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    commentaire = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_published = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.Sujet}'