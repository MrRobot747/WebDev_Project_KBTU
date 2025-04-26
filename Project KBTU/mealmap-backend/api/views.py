from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Recipe, MealPlan, ShoppingList
from .serializers import RecipeSerializer, RecipeCreateSerializer, MealPlanSerializer, ShoppingListSerializer

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Recipe
from .serializers import RecipeSerializer

@api_view(['GET'])
def recipe_list(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def recipe_detail(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

# FBV: list/create recipes
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def recipe_list(request):
    if request.method == 'GET':
        qs = Recipe.objects.filter(user=request.user)
        serializer = RecipeSerializer(qs, many=True)
        return Response(serializer.data)
    serializer = RecipeCreateSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# FBV: detail/update/delete
@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def recipe_detail(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk, user=request.user)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    recipe.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# CBV: MealPlan list/create
class MealPlanView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        plans = MealPlan.objects.filter(user=request.user)
        serializer = MealPlanSerializer(plans, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = MealPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# CBV: ShoppingList CRUD
class ShoppingListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, plan_id):
        sl = ShoppingList.objects.filter(mealplan_id=plan_id)
        serializer = ShoppingListSerializer(sl, many=True)
        return Response(serializer.data)
    def post(self, request, plan_id):
        sl = ShoppingList.objects.create(mealplan_id=plan_id)
        serializer = ShoppingListSerializer(sl)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


