from django.urls import path
from .views import ListCommentsView, CreateCommentView, RetrieveCommentView, UpdateCommentView, DeleteCommentView

urlpatterns = [
    path('tasks/<int:task_id>/', ListCommentsView.as_view(), name='list_comments'),
    path('tasks/<int:task_id>/create/', CreateCommentView.as_view(), name='create_comment'),
    path('<int:id>/', RetrieveCommentView.as_view(), name='retrieve_comment'),
    path('<int:id>/update/', UpdateCommentView.as_view(), name='update_comment'),
    path('<int:id>/delete/', DeleteCommentView.as_view(), name='delete_comment'),
]
