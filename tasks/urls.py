from django.urls import path
from tasks.views import show_task,show_specific_task,dashboard
urlpatterns = [
    path("show-task/",show_task),
    path("show_task/<int:id>",show_specific_task),
    path("Dashboard/",dashboard)

]