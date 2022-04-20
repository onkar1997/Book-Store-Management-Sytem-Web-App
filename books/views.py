from django.shortcuts import render, redirect, get_object_or_404
from stores.models import Store
from books.models import Book
from django.contrib import messages
import datetime
from django.templatetags.static import static


def go_back(request, id):
    store = Store.objects.get(id=id)
    return render(request, '/'+str(store.id))


def add_book_page(request, book_id):
    store = Store.objects.filter(id=book_id)
    return render(request, 'books/add_book.html', {'store': store})


def add_book(request, book_id):
    if(request.method == 'POST'):
        book_name = request.POST['book_name']
        author_name = request.POST['author_name']
        publisher_name = request.POST['publisher_name']
        num_of_copies = request.POST['num_of_copies']
        price = request.POST['price']
        book_image = request.FILES['book_image']
        pub_date = datetime.datetime.now()
        store_id = book_id

        book = Book(book_name=book_name, author_name=author_name, publisher_name=publisher_name,
                    num_of_copies=num_of_copies, price=price, book_image=book_image, pub_date=pub_date, store_id=store_id)
        book.save()

        messages.success(request, "Book Added Successfully")
        return redirect('/'+str(store_id))
    else:
        messages.success(request, "Oops! Something went wrong. Try again...")
        return render(request, '/')


def edit_book(request, store_id, book_id):
    store = Store.objects.get(id=store_id)
    book = Book.objects.get(id=book_id)
    return render(request, 'books/edit_book.html', {'store': store, 'book': book})


def edit_go_back(request, store_id, book_id):
    return render(request, '/'+str(store.id))


def update_book(request, id):
    book = Book.objects.get(id=id)
    if(request.method == 'POST'):
        book.book_name = request.POST['book_name']
        book.author_name = request.POST['author_name']
        book.publisher_name = request.POST['publisher_name']
        book.num_of_copies = request.POST['num_of_copies']
        book.book_image = request.FILES['book_image']
        book.price = request.POST['price']
        book.pub_date = datetime.datetime.now()

        book.save()

        messages.success(request, "Book Updated Successfully.")
        return redirect('/'+str(book.store_id))
    else:
        messages.error(request, "Oops! something went wrong")
        return render(request, 'books/edit_book.html')


def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()

    messages.success(request, "Book Deleted Successfully.")
    return redirect('/'+str(book.store_id))
