from django.db import models

# Create your models here.
class Dmodels(models.Model):
    title = models.CharField(max_length=30)
    last_update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "3D model"
        verbose_name_plural = "3D modellar"