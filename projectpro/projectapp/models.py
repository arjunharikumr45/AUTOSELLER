from django.db import models
class data(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.CharField(max_length=500)
    Image=models.ImageField(upload_to='images/')
    is_sedan=models.BooleanField(default=False)
    is_hatchback=models.BooleanField(default=False)
    is_premium=models.BooleanField(default=False)
    def __str__(self):
        return self.name


