from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='welcome'),

    path('home', views.home, name='home'),

    # Stores
    path('<int:store_id>', views.view_books, name='view_books'),

    path('add_store', views.add_store, name='add_store'),

    path('<int:store_id>/edit_store', views.edit_store, name='edit_store'),

    path('<int:store_id>/update_store',
         views.update_store, name='update_store'),

    path('<int:store_id>/delete_store', views.delete_store, name='delete_store'),

]
