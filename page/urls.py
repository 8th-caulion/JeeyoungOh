from django.urls import path
from . import views
import accounts.views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/<int:blog_id>', views.detail, name="detail"),
    path('blog/new/', views.new, name="new"),
    path('blog/create/', views.create, name="create"),
    path('blog/update/<int:blog_id>/', views.update, name="update"),
    path('blog/edit/<int:blog_id>/', views.edit, name="edit"),
    path('blog/delete/<int:blog_id>/', views.delete, name="delete"),

    path('signup/',accounts.views.signup, name="signup"),
    path('login/',accounts.views.login, name="login"),
]