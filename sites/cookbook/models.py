from django.db import models


class Ingredient(models.Model):
    name = models.CharField(verbose_name='Ингредиент', max_length=32)


class Recipe(models.Model):
    name = models.CharField(verbose_name='Рецепт', max_length=32)


class IngredientInRecipes(models.Model):
    ingredient = models.ForeignKey('Ingredient', verbose_name='Ингредиент id', on_delete=models.CASCADE)
    recipe = models.ForeignKey('Recipe', verbose_name='Рецепт id', on_delete=models.CASCADE)
    count = models.PositiveIntegerField(verbose_name='Количество')


class Log(models.Model):
    request = models.CharField(verbose_name='Запрос', max_length=256)
    result = models.TextField(verbose_name='Результат', max_length=256)
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True, db_index=True)
