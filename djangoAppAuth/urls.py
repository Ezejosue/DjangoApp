"""
URL configuration for djangoAppAuth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('task/', views.tasks, name='task'),
    path('task/completed', views.tasksCompleted, name='taskCompleted'),
    path('logout/', views.logoutUser, name='logout'),
    path('login/', views.loginView, name='login'),
    path('task/createTask', views.task_create, name='createTask'),
    path('task/detailTask/<int:id>', views.task_detail, name='detailTask'),
    path('task/detailTask/<int:id>/complete',
         views.task_complete, name='completeTask'),
    path('task/detailTask/<int:id>/delete',
         views.task_delete, name='deleteTask'),

]
