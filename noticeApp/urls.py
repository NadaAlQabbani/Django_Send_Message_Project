from django.urls import path ,re_path
from . import views

app_name = "noticeApp"

urlpatterns = [
    path('',views.index, name='index'),
]

