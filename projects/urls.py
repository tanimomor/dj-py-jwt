from django.urls import path
from .views import ListProjectsView, CreateProjectView, RetrieveProjectView, UpdateProjectView, DeleteProjectView

urlpatterns = [
    path('', ListProjectsView.as_view(), name='list_projects'),
    path('create/', CreateProjectView.as_view(), name='create_project'),
    path('<int:id>/', RetrieveProjectView.as_view(), name='retrieve_project'),
    path('<int:id>/update/', UpdateProjectView.as_view(), name='update_project'),
    path('<int:id>/delete/', DeleteProjectView.as_view(), name='delete_project'),
]
