# Generated by Django 3.0.2 on 2020-02-01 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Ингредиент')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.CharField(max_length=256, verbose_name='Запрос')),
                ('result', models.TextField(max_length=256, verbose_name='Результат')),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Рецепт')),
            ],
        ),
        migrations.CreateModel(
            name='IngredientInRecipes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(verbose_name='Количество')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.Ingredient', verbose_name='Ингредиент id')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.Recipe', verbose_name='Рецепт id')),
            ],
        ),
    ]