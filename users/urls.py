from django.urls import path
from users import views

urlpatterns = [
    path('home', views.home,name='home-page'),
    path('success/', views.success,name='success-page'),
    path('register/', views.register,name='register-page'),
    path('login/', views.user_login,name='login-page'),
    path('logout/', views.user_logout,name='logout-page'),
    path('user/logout/', views.gts,name='gts'),
    
    
]
