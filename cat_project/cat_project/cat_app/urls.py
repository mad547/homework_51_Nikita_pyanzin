from django.urls import path

from cat_app.views import index, cat_stats


urlpatterns = [
    path('', index, name='index'),
    path('cat_stats/', cat_stats, name='cat_stats'),
]