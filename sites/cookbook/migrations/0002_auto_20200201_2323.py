from django.db import migrations


def fill_book(apps, schema_editor):
    Ingredient = apps.get_model('cookbook', 'Ingredient')
    Recipe = apps.get_model('cookbook', 'Recipe')
    IngredientInRecipes = apps.get_model('cookbook', 'IngredientInRecipes')

    ingredient_in_recipe = [
        {
            'name': 'Салат «Русский»',
            'components': [
                {
                    'item': 'мясо',
                    'q': 250
                },
                {
                    'item': 'огурец',
                    'q': 2
                }
            ]
        },
        {
            'name': 'Салат «Ленинградский»',
            'components': [
                {
                    'item': 'мясо',
                    'q': 500
                },
                {
                    'item': 'картофель',
                    'q': 3
                }
            ]
        },
        {
            'name': 'Салат с рыбой и овощами',
            'components': [
                {
                    'item': 'рыба',
                    'q': 500
                },
                {
                    'item': 'картофель',
                    'q': 10
                },
                {
                    'item': 'яйцо',
                    'q': 3
                }
            ]
        },
    ]

    for i_in_r in ingredient_in_recipe:
        recipe, _ = Recipe.objects.get_or_create(name=i_in_r['name'])
        for c in i_in_r['components']:
            ingredient, _ = Ingredient.objects.get_or_create(name=c['item'])
            count = c['q']
            IngredientInRecipes.objects.create(ingredient=ingredient, recipe=recipe, count=count)


def rollback_fill(apps, schema_editor):
    Ingredient = apps.get_model('cookbook', 'Ingredient')
    Recipe = apps.get_model('cookbook', 'Recipe')
    IngredientInRecipes = apps.get_model('cookbook', 'IngredientInRecipes')

    IngredientInRecipes.objects.all().delete()
    Ingredient.objects.all().delete()
    Recipe.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fill_book, rollback_fill),
    ]
