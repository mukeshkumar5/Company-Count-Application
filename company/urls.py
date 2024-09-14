from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list_view, name='user_list'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('upload/', views.upload_file, name='upload'),
    path('query/', views.query_companies, name='query_companies'),
    path('query_builder/', views.query_builder_view, name='query_builder'),
]
