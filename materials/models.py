from django.db import models


# Наследуемся от models.Model чтобы сразу к БД подтянулась
class Material(models.Model):
    title = models.CharField(max_length=256)
    desc = models.CharField(max_length=1024)
    url = models.CharField(max_length=1024)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.title
