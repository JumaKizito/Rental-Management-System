from django.urls import path
from . import views


urlpatterns = [
path('', views.dashboard_view, name='dashboard'),
path('properties/', views.property_list, name='property_list'),
path('properties/create/', views.property_create, name='property_create'),
path('properties/<int:pk>/', views.property_detail, name='property_detail'),
path('properties/<int:pk>/edit/', views.property_update, name='property_update'),
path('properties/<int:pk>/delete/', views.property_delete, name='property_delete'),
path('logout/', views.logout_view, name='logout'),

]