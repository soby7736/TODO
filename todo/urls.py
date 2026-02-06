"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from user_app.views import *
from user_task.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',RegisterView.as_view(),name="signup"),
    path('sign/',Signin.as_view(),name="signin"),
    path('logout/', LogoutView.as_view(),name="logout"),
    path('add/', AddTaskView.as_view(),name="add_task"),
    path('view/',TaskView.as_view(),name="task_view"),
    path('update/<int:pk>',TaskUpdateView.as_view(),name="update_view"),
    path("",BaseView.as_view(),name="home"),
    path('delete/<int:pk>',TaskDelete.as_view(),name="task_delete"), 
    path('complete/<int:pk>',TaskCompleteView.as_view(),name="complete"), 
    path('search/',SearchView.as_view(),name="search")
]
