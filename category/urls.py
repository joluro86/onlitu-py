from category.views import add_category,  edit_category, categories, delete_category

from django.urls import path

urlpatterns = [
    path('crear/', add_category, name='add-category'),
    path('editar/<int:id>/edit/', edit_category, name='edit-category'),
    path('', categories, name='categories'),
    path('eliminar/<int:id>/delete/', delete_category, name='delete-category'),
]