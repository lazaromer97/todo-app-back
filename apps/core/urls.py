from django.urls import path
from .api import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    # Task
    path('tasks/', TaskList.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('tasks/add/', TaskCreate.as_view(), name='task_create'),
    path('tasks/update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('tasks/delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),
]
