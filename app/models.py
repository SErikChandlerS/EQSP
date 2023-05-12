from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.full_name
