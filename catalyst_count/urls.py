from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from company import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('api/', include('company.urls')),
]
