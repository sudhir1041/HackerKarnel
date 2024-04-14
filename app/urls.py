from django.contrib import admin
from django.urls import path
from .views import home
from .views import AddUser
from .views import AddTask
from .views import UserList
from .views import TaskList
from .views import exportExcel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('AddUser',AddUser,name='AddUser'),
    path('AddTask',AddTask,name='AddTask'),
    path('UserList',UserList,name='UserList'),
    path('TaskList',TaskList,name='TaskList'),
    path('exportExcel',exportExcel,name='exportExcel'),
    
]
