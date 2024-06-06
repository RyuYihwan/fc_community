from django.urls import path, include

from board import views

urlpatterns = [
    path('detail/<int:pk>/', views.board_details),
    path('list/', views.board_list),
    path('write/', views.board_write, name='write'),
]
