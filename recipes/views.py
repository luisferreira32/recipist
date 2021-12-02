from django.shortcuts import render, get_object_or_404
from django.views import generic, View

from .models import Recipe

class IndexView(generic.ListView):
    template_name = 'recipes/index.html'
    context_object_name = 'recipes_list'
    paginate_by = 10

    def get_queryset(self):
        """Return all existing recipies."""
        return Recipe.objects.all()


class RecipeView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'
    

class OrderView(View):
    model = Recipe
    template_name = 'recipes/order.html'

    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        return render(request, self.template_name, {'recipe': recipe})

    def post(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        return render(request, self.template_name, {'recipe': recipe})
