from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('single/<int:pk>', views.post_single, name="post_single"),

    # path('', views.post_single, name='post_single'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
]