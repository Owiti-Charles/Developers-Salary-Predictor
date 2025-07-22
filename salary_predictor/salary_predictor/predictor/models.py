from django.db import models

class Countries(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class JobTitles(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


