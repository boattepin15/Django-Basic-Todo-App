from django.urls import path
from . import views
urlpatterns = [
    path('addtodo/', view=views.add_task, name='add-task'),
    path('mask_as_complate/<int:pk>/', view=views.mask_as_complate, name='mask_as_complate'),
    path('mask_as_doing/<int:pk>/', view=views.mask_as_doing, name='mask_as_doing'),
    path('delete_task/<int:pk>/', view=views.delete_task, name='delete_task'),
    path('edit_task/<int:pk>/', view=views.edit_task, name='edit_task'),
]
