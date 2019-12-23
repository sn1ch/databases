from django.shortcuts import render
from .models import Book
from datetime import datetime


def books_view(request):
    template = 'books/books_list.html'
    books = []
    for book in Book.objects.all():
        item = {
            'name': book.name,
            'author': book.author,
            'pub_date': book.pub_date.strftime("%Y-%m-%d")
        }
        books.append(item)
    context = {'books': books}
    return render(request, template, context)


def books_on_date_view(request, date=None):
    template = 'books/book_pub_date.html'
    books = []
    if date:
        for book in Book.objects.all().filter(pub_date=date):
            item = {
                'name': book.name,
                'author': book.author,
                'pub_date': book.pub_date.strftime("%Y-%m-%d")
            }
            books.append(item)

    sorted_pub_date_list = sorted([datetime.strftime(x[0], '%Y-%m-%d') for x in Book.objects.values_list('pub_date')])
    current_page = sorted_pub_date_list.index(date)
    if current_page + 1 < len(sorted_pub_date_list):
        next_page = sorted_pub_date_list[current_page + 1]
    else:
        next_page = None

    if current_page - 1 > -1:
        prev_page = sorted_pub_date_list[current_page - 1]
    else:
        prev_page = None

    context = {
        'books': books,
        'next_page': next_page,
        'prev_page': prev_page
    }
    return render(request, template, context)
