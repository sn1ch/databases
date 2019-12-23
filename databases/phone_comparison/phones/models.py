from django.db import models


# Create your models here.

class Phone(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    cpu = models.TextField()
    ram = models.TextField()
    display = models.TextField()

    def __str__(self):
        return self.name


class Samsung(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    other = models.TextField(default=None)



class Apple(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    other = models.TextField(default=None)
