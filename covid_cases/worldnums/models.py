from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=200)
    num = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
