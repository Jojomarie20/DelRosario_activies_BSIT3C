from django.urls import path
from .views import index, get_items, add_items, update_items, delete_items

app_name = "items"

urlpatterns = [
    path('', index, name='index'),
    path('<int:item_id>/', get_items, name='get_items'),
    path('add', add_items, name='add_items'),
    path('update/<int:item_id>/', update_items, name='update_items'),
    # path('delete/<int:item_id>/', delete_items, name='delete_items'),
    path('delete/<int:item_id>/', delete_items, name='delete_items'),
    # path('/items/<str:id>/', get_single_item, name='index')
]