from django.urls import path
from . import views


urlpatterns = [
    path('',views.todoApp),
    path('addInfo',views.addInfo,name='addInfo'),
    path('editInfo/<int:id>',views.editInfo,name='editInfo'),
    path('deleteInfo',views.deleteInfo,name='deleteInfo'),
    path('doneInfo/<int:id>',views.doneInfo,name='doneInfo'),
]
