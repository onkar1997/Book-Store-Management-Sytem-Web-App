from django.urls import path
from . import views

urlpatterns = [

    # Books
    path('<int:book_id>', views.go_back, name='go_back'),

    path('<int:book_id>/add_book_page',

         views.add_book_page, name='add_book_page'),

    path('add_book/<int:book_id>', views.add_book, name='add_book'),

    path('<int:store_id>/<int:book_id>/edit_book',
         views.edit_book, name='edit_book'),

    path('<int:store_id>', views.edit_go_back, name='edit_go_back'),

    path('<int:id>/update_book', views.update_book, name='update_book'),

    path('delete_book/<int:id>', views.delete_book, name='delete_book'),
]
