from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(3)], unique=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(3)], unique=True)

    def __str__(self):
        return self.title


class Todo(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(3)])
    description = models.CharField(max_length=2000)
    due_date = models.DateTimeField('due date')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
