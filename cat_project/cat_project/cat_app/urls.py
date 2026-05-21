from django.urls import path

from cat_app.views import index,cat_list, cat_stats


urlpatterns = [
    path('', index, name='index'),
    path('cats/', cat_list, name='cats_list'),
    path('cats/<int:cat_index>/', cat_stats, name='cat_stats'),
]