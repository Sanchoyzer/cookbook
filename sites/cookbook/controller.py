import json
from typing import Dict, Set

from django.db.models import Count

from .models import Ingredient, IngredientInRecipes, Log, Recipe


class CookController:
    @classmethod
    def _get_refrigerator(cls, data: Dict) -> Dict[int, float]:
        # TODO: may be use Serializers?
        result = dict()
        for ingredient, count in data.items():
            try:
                ingredient_obj = Ingredient.objects.get(name=ingredient)
            except Ingredient.DoesNotExist:
                raise ValueError(f'invalid ingredient "{ingredient}"')

            try:
                count = float(count)
                if count <= 0:
                    raise ValueError('negative')
            except ValueError:
                raise ValueError(f'invalid count "{count}"')

            result[ingredient_obj.id] = count
        return result

    @classmethod
    def _get_available_recipes(cls, refrigerator: Dict) -> Set[int]:
        result = set()
        recipes_with_ingredients = {}

        qs = IngredientInRecipes.objects \
            .filter(ingredient__in=refrigerator.keys()) \
            .values('recipe') \
            .annotate(ing_count=Count('ingredient'))
        for ing_in_rec in qs:
            recipes_with_ingredients[ing_in_rec['recipe']] = ing_in_rec['ing_count']

        qs = IngredientInRecipes.objects \
            .filter(recipe__in=recipes_with_ingredients.keys()) \
            .values('recipe') \
            .annotate(ing_count=Count('ingredient'))
        for ing_in_rec in qs:
            recipe_id = ing_in_rec['recipe']
            if ing_in_rec['ing_count'] == recipes_with_ingredients[recipe_id]:
                result.add(recipe_id)
        return result

    @classmethod
    def _get_portions(cls, recipes_id: Set[int], refrigerator: Dict) -> Dict[str, int]:
        portions = {}
        for recipe_id in recipes_id:
            portions_count = set()
            for ing_in_rec in IngredientInRecipes.objects.filter(recipe=recipe_id):
                recipe_count = ing_in_rec.count
                refrigerator_count = refrigerator[ing_in_rec.ingredient.id]
                portions_count.add(int(refrigerator_count // recipe_count))
            portions[recipe_id] = min(portions_count)

        return {Recipe.objects.get(id=r).name: cnt for r, cnt in portions.items() if cnt > 0}

    @classmethod
    def _add_to_log(cls, request: Dict, result: Dict) -> None:
        Log.objects.create(request=json.dumps(request), result=json.dumps(result))

    @classmethod
    def what_can_i_cook(cls, data: Dict) -> Dict[str, int]:
        refrigerator = cls._get_refrigerator(data=data)
        available_recipes_id = cls._get_available_recipes(refrigerator=refrigerator)
        result = cls._get_portions(recipes_id=available_recipes_id, refrigerator=refrigerator)
        cls._add_to_log(request=data, result=result)
        return result
