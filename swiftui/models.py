from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    active = models.BooleanField()
    balance = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
