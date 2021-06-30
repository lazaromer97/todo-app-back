from django.urls import path
from .api import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CommentList, CommentDetail, CommentCreate, CommentUpdate, CommentDelete

urlpatterns = [
    # Task
    path('tasks/', TaskList.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('tasks/add/', TaskCreate.as_view(), name='task_create'),
    path('tasks/update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('tasks/delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),

    # Comment
    path('comments/', CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment_detail'),
    path('comments/add/', CommentCreate.as_view(), name='comment_create'),
    path('comments/update/<int:pk>/', CommentUpdate.as_view(), name='comment_update'),
    path('comments/delete/<int:pk>/', CommentDelete.as_view(), name='comment_delete'),
]
