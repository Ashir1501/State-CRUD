from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=100)
    population = models.PositiveBigIntegerField(default=1)
    language = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)

    class Meta:
        db_table = 'State'

    def __str__(self):
        return self.name