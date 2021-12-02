from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=100, default="Food")
    steps = models.TextField()

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Nothing")
    amount = models.FloatField()
    unit = models.CharField(max_length=20)
