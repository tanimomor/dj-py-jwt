from django.urls import path
from .views import ListTasksView, CreateTaskView, RetrieveTaskView, UpdateTaskView, DeleteTaskView

urlpatterns = [
    path('projects/<int:project_id>/', ListTasksView.as_view(), name='list_tasks'),
    path('projects/<int:project_id>/create/', CreateTaskView.as_view(), name='create_task'),
    path('<int:id>/', RetrieveTaskView.as_view(), name='retrieve_task'),
    path('<int:id>/update/', UpdateTaskView.as_view(), name='update_task'),
    path('<int:id>/delete/', DeleteTaskView.as_view(), name='delete_task'),
]
