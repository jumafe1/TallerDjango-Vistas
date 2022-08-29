from django.db import models

class Variable(models.Model):
    name = models.CharField(primary_key= True,max_length=50)

    def __str__(self):
        return '{}'.format(self.name)