from django.shortcuts import render, redirect, get_object_or_404
from stores.models import Store
from books.models import Book
from django.contrib import messages
import datetime
from django.templatetags.static import static


def index(request):
    return render(request, 'welcome.html')


def home(request):
    if request.user.is_authenticated:
        store_list = Store.objects.filter(user=request.user)
        return render(request, 'index.html', {'store_list': store_list})
    else:
        store_list = Store.objects.all()
        return render(request, 'index.html', {'store_list': store_list})


def view_books(request, store_id):
    store_list = Store.objects.filter(id=store_id)
    book_list = Book.objects.filter(store_id=store_id)
    return render(request, 'stores/view_books.html', {'store_list': store_list, 'book_list': book_list})


def add_store(request):
    if(request.method == 'POST'):
        store_name = request.POST['name']
        owner_name = request.POST['owner_name']
        address = request.POST['address']
        store_image = request.FILES['store_image']
        pub_date = datetime.datetime.now()
        user_id = request.user.id
        user = request.user

        store = Store(store_name=store_name, owner_name=owner_name,
                      address=address, store_image=store_image, pub_date=pub_date, user_id=user_id)
        store.save()

        messages.success(request, "Store Added Successfully.")
        return redirect('home')
    else:
        return render(request, 'stores/add_store.html')


def edit_store(request, store_id):
    store = Store.objects.get(id=store_id)
    return render(request, 'stores/edit_store.html', {'store': store})


def update_store(request, store_id):
    store = Store.objects.get(id=store_id)
    if(request.method == 'POST'):
        store.store_name = request.POST['name']
        store.owner_name = request.POST['owner_name']
        store.address = request.POST['address']
        store.store_image = request.FILES['store_image']
        store.pub_date = datetime.datetime.now()
        store.save()

        messages.success(request, "Store Updated Successfully.")
        return redirect('home')
    else:
        messages.error(request, "Oops! something went wrong")
        return render(request, 'stores/edit_store.html')


def delete_store(request, store_id):
    store = Store.objects.get(id=store_id)
    store.delete()

    messages.success(request, "Store Deleted Successfully.")
    return redirect('home')
