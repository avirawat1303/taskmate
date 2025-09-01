from todolist import views
from django.urls import path
urlpatterns = [
    path("",views.todolist, name='todolist'),
    path("delete/<int:id>", views.delete_task,name="delete_task"),
    path("complete/<int:id>", views.complete_task,name="complete_task"),
    path("pending/<int:id>", views.pending_task,name="pending_task"),
    path("edit/<int:id>", views.edit_task ,name="edit_task"),
]

#vairable to map id to url--<int.id>
