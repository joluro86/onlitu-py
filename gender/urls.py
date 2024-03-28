from gender.views import add_gender, edit_gender, delete_gender, genders
from django.urls import path

urlpatterns = [
    path('', genders, name='genders'),
    path('crear/', add_gender, name='add-gender'),
    path('editar/<int:id>/edit/', edit_gender, name='edit-gender'),
    path('eliminar/<int:id>/delete/', delete_gender, name='delete-gender'),
]