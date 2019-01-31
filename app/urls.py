
from django.urls import path
from . import views
urlpatterns = [
path('', views.home, name = 'index'),
path('check/<list_id>', views.check, name = 'check'),
path('delete/<list_id>', views.delete, name = 'delete'),
path('edit/<list_id>', views.edit, name = 'edit'),
path('delete_chacked_items', views.delete_chacked_items, name = 'delete_chacked_items'),
path('post_new/<list_id>', views.post_new, name = 'post_new'),
]

