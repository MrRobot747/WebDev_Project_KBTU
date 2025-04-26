from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    calories = models.IntegerField()

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    calories_per_unit = models.FloatField()

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

class MealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    recipes = models.ManyToManyField(Recipe)

class ShoppingList(models.Model):
    mealplan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)