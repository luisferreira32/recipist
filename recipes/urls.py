from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('r<int:pk>/', views.RecipeView.as_view(), name='recipe'),
    path('r<int:pk>/order', views.OrderView.as_view(), name='order'),
]