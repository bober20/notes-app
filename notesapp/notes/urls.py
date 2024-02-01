from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
    path('', views.show_index_page, name='index'),
    path('home/', views.show_home_page, name='home_page'),
    path('add_note/', views.add_note, name='add_note'),
    path('info/<slug:slug>/', views.show_info, name='info'),
    path('delete/<slug:slug>/', views.delete_note, name='delete'),
    path('edit/<slug:slug>/', views.edit_note, name='edit')
]