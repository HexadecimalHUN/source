from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('cross_off/<list_id>', views.cross_off, name='cross_off'),
    path('uncross/<list_id>', views.uncross, name='uncorss'),
]