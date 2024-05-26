from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Kategoriyasi')
    published = models.BooleanField()

    def __str__(self):
        return self.name

class Cars(models.Model):
    name = models.CharField(max_length=150, verbose_name='Mashina nomi')
    colors = models.CharField(max_length=15)
    speed = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published = models.BooleanField()


    def __str__(self):
        return self.name