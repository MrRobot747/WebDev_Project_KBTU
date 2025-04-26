from rest_framework import serializers
from .models import Recipe, Ingredient, MealPlan, ShoppingList, RecipeIngredient
from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

# Serializer.Serializer examples
class IngredientSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    calories_per_unit = serializers.FloatField()

class RecipeCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    calories = serializers.IntegerField()
    ingredients = IngredientSerializer(many=True)

    def create(self, validated_data):
        user = self.context['request'].user
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(user=user, **validated_data)
        for ing in ingredients_data:
            i, _ = Ingredient.objects.get_or_create(**ing)
            RecipeIngredient.objects.create(recipe=recipe, ingredient=i, quantity=ing.get('quantity', 1))
        return recipe

# ModelSerializer examples
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'calories']

class MealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPlan
        fields = ['id', 'date', 'recipes']

class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ['id', 'mealplan', 'created']