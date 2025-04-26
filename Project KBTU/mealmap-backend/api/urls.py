from django.urls import path
from .views import recipe_list, recipe_detail, MealPlanView, ShoppingListView
from django.urls import path
from .views import recipe_list, recipe_detail

urlpatterns = [
    path('recipes/', recipe_list, name='recipe-list'),
    path('recipes/<int:pk>/', recipe_detail, name='recipe-detail'),
]

urlpatterns = [
    path('recipes/', recipe_list, name='recipe-list'),
    path('recipes/<int:pk>/', recipe_detail, name='recipe-detail'),
    path('mealplans/', MealPlanView.as_view(), name='mealplan-list'),
    path('mealplans/<int:plan_id>/shoppinglists/', ShoppingListView.as_view(), name='shoppinglist'),
]
