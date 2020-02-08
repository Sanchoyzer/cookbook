from django.contrib import admin

from .models import Ingredient, Recipe, IngredientInRecipes, Log


admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(IngredientInRecipes)
admin.site.register(Log)
