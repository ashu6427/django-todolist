from django.urls import path, reverse_lazy
from . import views
from base.views import TaskList, TaskDetail, TaskCreate, UpdateTask, DeleteTask, CustomLoginView, CustomLogoutView, RegisterPage
from django.contrib.auth.views import LogoutView

# urls for base app
urlpatterns = [
    # path('logout/', LogoutView.as_view(next_page='login'), name = 'logout'),
    # The above path is a direct method to logout the user without writing the code in views

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', UpdateTask.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteTask.as_view(), name='task-delete'),
]
