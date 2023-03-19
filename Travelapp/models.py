from django.db import models

# Create your models here.


class Table1(models.Model):
    Name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='Pictures')
    desc = models.TextField()

    def __str__(self):
        return self.Name


class Table2(models.Model):
    Name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='Photos')
    details = models.TextField()

    def __str__(self):
        return self.Name

