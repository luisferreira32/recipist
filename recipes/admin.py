from django.contrib import admin

from .models import Recipe, Ingredient

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 3

class RecipeAdmin(admin.ModelAdmin):
    fields = ['name', 'steps']
    inlines = [IngredientInline]

admin.site.register(Recipe, RecipeAdmin)
