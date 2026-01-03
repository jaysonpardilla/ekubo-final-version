from django.urls import path
from . import views

app_name = 'shops'
urlpatterns = [
    path('', views.shops_list, name='shops_list'),
    path('update-shop-informations/<str:pk>/', views.update_shop, name='update_shop'),
    path('view-shop/<str:pk>/', views.view_shop, name='view_shop'),
]






